<<<<<<< HEAD
from face_recognition.api import face_locations
import numpy as np
import cv2
import imutils
from PIL import ImageGrab, Image
from pymysql import connect
import imgDB
import deleteFile
from os import listdir
from os.path import isdir, isfile, join
import os

def train(name):
    data_path = path = os.getcwd() + "\\"
    face_pic = [f for f in lisdir(data_path) if isfile(join(data_path, f))]
    train_data, labels = [], []

    for i, files in enumerate(face_pic):
        image_path = data_path + face_pic[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if images is None:
            continue
        train_data.append(np.asarray(images, dtype=np.uint8))
        labels.append(i)
    if len(labels) == 0:
        print("there is no data to train")
        return None
    labels = np.asarray(labels, dtype=np.int32)
    model = cv2.face.LBPHFaceRcognizer_create()
    model.train(np.asarray(train_data), np.asarray(labels))
    print(name + " : model training complete")
=======
import numpy as np
import cv2
import imutils
from PIL import Image
import pymysql
import imgDB
import deleteFile
from os import listdir
from os.path import isfile, join
import os
import string
import imageio

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

def who_are(frame, startX, startY, endX, endY):
    name=1
    #얼굴 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    roi = frame[startY:endY, startX:endX]
    roi = cv2.resize(roi, (200, 200))

    min_score=999
    min_score_name=""
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    model = cv2.face.LBPHFaceRecognizer_create()

    models = imgDB.callResult()

    if not models:
        imgDB.creTable(("n" + str(name)))
        imgDB.imgToDB(("n" + str(name)), frame[startY:endY, startX:endX])
        imgDB.imgFromDB(("n" + str(name)))
        train().write("samples\\"+('n'+str(name))+".yml")
        imgDB.saveResult(("n" + str(name)), os.getcwd() + "\samples\\" + ('n'+str(name)) + ".yml")
        deleteFile.delImg("1")
        name = name+1
        return 0
    
    else:
        for key, paths in models.items():
            model.read(paths)
            result = model.predict(roi)
            if min_score>result[1]:
                min_score = result[1]
                min_score_name = key
                name = int((list(key))[1]) + 1
        
        if min_score<100:
            confidence = result
            display_string = str(confidence)+ " confidence it is" + min_score_name
            cv2.putText(frame, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)
       # if confidence>75:
            cv2.putText(frame, min_score_name, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            imgDB.imgToDB(str(min_score_name), frame[startY:endY, startX:endX])
            imgDB.imgFromDB(str(min_score_name))
            os.remove("samples\\"+str(min_score_name)+".yml")
            train().write("samples\\"+(str(min_score_name))+".yml")
            path = os.getcwd() + "\image\\"
            onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
            imgDB.saveResult(str(min_score_name), os.getcwd() + "\samples\\" + (str(min_score_name)) + ".yml")
            for i, files in enumerate(onlyfiles):
                image_path=path+onlyfiles[i]
                deleteFile.delImg(onlyfiles[i])

        else:
            for key, paths in models.items():
                name = int((list(key))[1]) + 1
            imgDB.creTable(("n" + str(name)))
            imgDB.imgToDB(("n" + str(name)), frame[startY:endY, startX:endX])
            imgDB.imgFromDB(("n" + str(name)))
            train().write("samples\\"+('n'+str(name))+".yml")
            imgDB.saveResult(("n" + str(name)), os.getcwd() + "\samples\\" + ('n'+str(name)) + ".yml")
            deleteFile.delImg("1")
            name = name+1
>>>>>>> e26ae08cecfedbb54202c8b448264031283648da
