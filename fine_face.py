import numpy as np
import cv2
import imutils
from PIL import ImageGrab, Image
from pymysql import connect
import imgDB
import deleteFile
import who
import hahaha

protoPath = "deploy.prototxt"
modelPath = "res10_300x300_ssd_iter_140000.caffemodel"
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

cam = cv2.VideoCapture("two_person.mp4")

imgDB.creTable2()

while True:
    img, frame = cam.read()

    if type(frame) == type(None):
        break

    frame = imutils.resize(frame, width=600)
    (h, w) = frame.shape[:2]

    imageBlob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB=False, crop=False)
    
    detector.setInput(imageBlob)
    detections = detector.forward()

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5 :
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            face = frame[startY:endY, startX:endX]
            (fH, fW) = face.shape[:2]

            if fW < 20 or fH < 20 :
                continue

            #faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96), (0, 0, 0), swapRB = True, crop = False)

            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
            
            #face_region = frame[startY:endY, startX:endX]
            #M = face_region.shape[0]
            #N = face_region.shape[1]
            #face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
            #face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
            #frame[startY:endY, startX:endX] = face_region

            #who.who_are(frame, startX, startY, endX, endY)
            hahaha.who_are(frame, startX, startY, endX, endY)

    cv2.imshow('Face',frame)
    if cv2.waitKey(1)==27:
        break

cam.release()
cv2.destroyAllWindows()