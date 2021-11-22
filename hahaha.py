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
