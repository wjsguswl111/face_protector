<<<<<<< HEAD
import cv2
import numpy as np
import os
from pkg_resources import resource_filename, Requirement

is_initialized = False
prototxt = None
caffemodel = None
net = None

threshold=0.5
enable_gpu=False

cam = cv2.VideoCapture("see.mp4")

while True:
    img, frame = cam.read()

    if not is_initialized:

        # access resource files inside package
        prototxt = "deploy.prototxt"
        caffemodel = "res10_300x300_ssd_iter_140000.caffemodel"
        
        # read pre-trained wieights
        net = cv2.dnn.readNetFromCaffe(prototxt, caffemodel)
    
        is_initialized = True

    # enable GPU if requested
    if enable_gpu:
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    
    (h, w) = frame.shape[:2]

    # preprocessing input image
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300,300), (104.0,177.0,123.0))
    net.setInput(blob)

    # apply face detection
    detections = net.forward()

    faces = []
    confidences = []

    # loop through detected faces
    for i in range(0, detections.shape[2]):
        conf = detections[0,0,i,2]

        # ignore detections with low confidence
        if conf < threshold:
            continue

        # get corner points of face rectangle
        box = detections[0,0,i,3:7] * np.array([w,h,w,h])
        (startX, startY, endX, endY) = box.astype('int')

        faces.append([startX, startY, endX, endY])
        confidences.append(conf)

        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)

            

    cv2.imshow('Face',frame)
    if cv2.waitKey(1)==27:
        break

cam.release()
cv2.destroyAllWindows()
=======
from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("즐겨찾기")
root.geometry("640x480+400+100") #창크키 and 위치 조정

root.resizable(False, False) #창 크기 변경 불가

pilimg = Image.open("C:\choun2.jpg")
phoimg = ImageTk.PhotoImage(pilimg)

img_var = StringVar()
btn_img1 = Checkbutton(root, text="img1", image = phoimg, onvalue = pilimg, variable=img_var)
btn_img2 = Checkbutton(root, text="img2", variable=img_var)
btn_img3 = Checkbutton(root, text="img3", variable=img_var)

btn_img1.deselect()
btn_img2.deselect()
btn_img3.deselect()

btn_img1.pack(anchor='center') #위치
btn_img2.pack()
btn_img3.pack()

def btncmd():
    print(img_var.get())

btn1 = Button(root, text="버튼1", command= btncmd)
btn1.pack()


root.mainloop()
>>>>>>> da1a815f7434dbeeffdcfba8ff4162e9f705d2fd
