import numpy as np
import cv2
import imutils
from PIL import ImageGrab, Image
from pymysql import connect
import imgDB
import pymysql
from os import listdir
from os.path import isfile, join
import os
import imageio
import GUI


def train():
    path = os.getcwd() + "\image\\"
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    Training_Data, Labels = [], []
    for i, files in enumerate(onlyfiles):
        image_path = path + onlyfiles[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if images is None:
            continue
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
    if len(Labels)==0:
        return None   
    Labels = np.asarray(Labels, dtype=np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(Training_Data), np.asarray(Labels))
    return model

def classify():
    protoPath = "deploy.prototxt"
    modelPath = "res10_300x300_ssd_iter_140000.caffemodel"
    detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

    video = cv2.VideoCapture(GUI.filename)
    while True:
        img, frame = video.read()

        if type(frame) == type(None):
            break

        frame = imutils.resize(frame, width=400)
        (h, w) = frame.shape[:2]

        imageBlob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
        
        detector.setInput(imageBlob)
        detections = detector.forward()

        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 0.5 :
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                (startX, startY) = (max(0, startX), max(0, startY))
                (endX, endY) = (min(w-1, endX), min(h-1, endY))
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                roi = frame[startY:endY, startX:endX]
                roi = cv2.resize(roi, (200, 200))

                min_score=999
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                
                model = cv2.face.LBPHFaceRecognizer_create()

                models = imgDB.callResult()

                for key, paths in models.items():
                    model.read(paths)
                    result = model.predict(roi)
                    if min_score>result[1]:
                        min_score = result[1]
                    
                if min_score<500:
                    confidence = int(100*(1-(min_score)/300))
                if confidence<70:
                    face_region = frame[startY:endY, startX:endX]
                    M = face_region.shape[0]
                    N = face_region.shape[1]
                    face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
                    face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
                    frame[startY:endY, startX:endX] = face_region

        cv2.imshow('Face',frame)
        if cv2.waitKey(1)==27:
            break

    video.release()
    cv2.destroyAllWindows()
    imgDB.cleanMember()