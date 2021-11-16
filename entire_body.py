import os
import cv2
import imutils

cap = cv2.VideoCapture('C:/Users/wjsgu/Desktop/test.avi')
font = cv2.FONT_HERSHEY_SIMPLEX #사람 감지 글씨체 정의

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
lower_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
upper_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

while True:
    ret, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayframe, 1.1, 2, 0, (20, 20))
    #lower = lower_cascade.detectMultiScale(grayframe, 1.8, 2, 0, (30, 30))
    #upper = upper_cascade.detectMultiScale(grayframe, 1.8, 2, 0, (30, 30))
    #frame = imutils.resize(frame, width=1000, height=1000)


    if not ret:
        break
    
    #frame = imutils.resize(frame, width=800, height=800)
    detected, _=hog.detectMultiScale(frame)

    '''for (x,y,w,h) in faces:
        for(x, y, w, h) in detected:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3, 4, 0)
        #cv2.putText(frame, (x-5, y-5), font, 0.9, (255,255,0),2)'''

    for(x, y, w, h) in detected:
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3, 4, 0)
        body_img=frame[y:y+h,x:x+w]
        body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
        body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
        frame[y:y+h,x:x+w] = body_img

    for(x, y, w, h) in faces:
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3, 4, 0)
        body_img=frame[y:y+h,x:x+w]
        body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
        body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
        frame[y:y+h,x:x+w] = body_img

    cv2.imshow("Detect", frame)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()


