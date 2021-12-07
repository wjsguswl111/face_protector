import numpy as np
import cv2
import imutils
<<<<<<< HEAD
from PIL import ImageGrab, Image
from pymysql import connect
=======
from PIL import Image
import pymysql
>>>>>>> e26ae08cecfedbb54202c8b448264031283648da
import imgDB
import deleteFile
from os import listdir
from os.path import isfile, join
import os
<<<<<<< HEAD
import fine_face as ff
import deleteFile

def train():
    path = os.getcwd() + "\\"
=======
import string
import imageio

def train():
    path = os.getcwd() + "\image\\"
>>>>>>> e26ae08cecfedbb54202c8b448264031283648da
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
<<<<<<< HEAD
        return None       
=======
        return None   
>>>>>>> e26ae08cecfedbb54202c8b448264031283648da
    Labels = np.asarray(Labels, dtype=np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(Training_Data), np.asarray(Labels))
    return model

def who_are(frame, startX, startY, endX, endY):
<<<<<<< HEAD
=======
    name=1
>>>>>>> e26ae08cecfedbb54202c8b448264031283648da
    #얼굴 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    roi = frame[startY:endY, startX:endX]
    roi = cv2.resize(roi, (200, 200))

    min_score=999
    min_score_name=""
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
<<<<<<< HEAD
    models = imgDB.callResult()

    for key, model in models.items():
        result = model.predict(roi)
        if not models:
            imgDB.creTable(str(ff.name))
            imgDB.imgToDB(str(ff.name), frame[startY:endY, startX:endX])
            imgDB.saveResulte(str(ff.name), model)
            ff.name+=1
        if min_score>result[1]:
            min_score = result[1]
            min_score_name = key
    
    if min_score<500:
        confidence = int(100*(1-(min_score)/300))
        display_string = str(confidence)+ " confidence it is" + min_score_name
    cv2.putText(frame, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)
    if confidence>75:
        cv2.putText(frame, min_score_name, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        imgDB.imgToDB(str(min_score_name), frame[startY:endY, startX:endX])
        imgDB.imgFromDB(str(min_score_name))
        train()
        path = os.getcwd() + "\\"
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        imgDB.saveResult(str(min_score_name), model)
        for i, files in enumerate(onlyfiles):
            image_path=path+onlyfiles[i]
            deleteFile.delImg(onlyfiles[i])

    else:
        imgDB.creTable(str(ff.name))
        imgDB.imgToDB(str(ff.name), frame[startY:endY, startX:endX])
        imgDB.saveResulte(str(ff.name), model)
        ff.name+=1
=======
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
        
        if min_score<500:
            confidence = int(100*(1-(min_score)/300))
            display_string = str(confidence)+ " confidence it is" + min_score_name
        cv2.putText(frame, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)
        if confidence>75:
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
