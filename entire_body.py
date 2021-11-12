#import os
import cv2
#import imutils

cap = cv2.VideoCapture('C:/Users/wjsgu/Desktop/test.avi')
hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    #frame = imutils.resize(frame, width=800, height=800)
    detected, _=hog.detectMultiScale(frame)

    for(x, y, w, h) in detected:
        #cv2.rectangle(frame, (x, y, w, h), (0, 255, 0), 3)
        body_img=frame[y:y+h,x:x+w]
        body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
        body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
        frame[y:y+h,x:x+w] = body_img

    cv2.imshow("Detect", frame)
    
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()