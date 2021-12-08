from array import array
import os
from PIL import Image, ImageDraw
import sys
import time
from io import BytesIO
import requests
import cv2
import io
import numpy as np
import test3
import imutils

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

def isSugg():
    cnt=0
    cap = cv2.VideoCapture('body.mp4')
    wid = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    hei = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWirter('output.avi',fourcc,30.0,(int(wid), int(hei)))
    x=1
    y=1
    w=1
    h=1

    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=600)

        if(cnt % 30 == 0):
            cnt=0

            cv2.imwrite("b1.jpg", frame)

            subscription_key = "49476384fc2548968bfc09ab465229ca"
            endpoint = "https://seungjoolee.cognitiveservices.azure.com/"

            print("===== Detect objects =====")
            analyze_url = endpoint + "vision/v3.1/analyze"
            image_data = open("b1.jpg", "rb").read()
            headers = {'Ocp-Apim-Subscription-Key': subscription_key,
                'Content-Type': 'application/octet-stream'}
            params = {'visualFeatures': 'objects'}
            response = requests.post(
                analyze_url, headers=headers, params=params, data=image_data)
            response.raise_for_status()
            analysis = response.json()
            #print(analysis.get('objects'))
            #li = []
        # draw = ImageDraw.Draw(image_data)

            objects = analysis['objects']
            name=0
            for obj in objects:
                if obj['object'] == 'person':
                    name+=1
                    rect = obj['rectangle']
                    x = rect['x']
                    y = rect['y']
                    w = rect['w']
                    h = rect['h']

                    #cv2.imwrite("ad1.jpg", frame[y:y+h, x:x+w])
                    ad, ra = test3.adult(frame[y:y+h, x:x+w], name)
                    if(ad == True or ra == True):
                        face_region = frame[y:y+h, x:x+w]
                        M = face_region.shape[0]
                        N = face_region.shape[1]
                        face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
                        face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
                        frame[y:y+h, x:x+w] = face_region
                    else:
                        x=1
                        y=1
                        w=1
                        h=1
                    
            os.remove("b1.jpg")
            #draw.rectangle(((x,y), (x+w, y+h)), outline='yellow')
        if x!=1 and y!=1 and w!=1 and h!=1:        
            face_region = frame[y:y+h, x:x+w]
            M = face_region.shape[0]
            N = face_region.shape[1]
            face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
            face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
            frame[y:y+h, x:x+w] = face_region
        
        cnt+=1
        if not ret:
            break
        cv2.imshow("body", frame)
        out.write(frame)
        if cv2.waitKey(1)==27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()