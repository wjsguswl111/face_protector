import os
import cv2
import imutils
#from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
#from PyQt5.QtCore import QUrl, QObject, pyqtSignal
#from testgui import CWidget


 
def blur(): 
    import testgui
    cap = cv2.VideoCapture(str(testgui.filename))
    font = cv2.FONT_HERSHEY_SIMPLEX #사람 감지 글씨체 정의

    fps = 20
    width = int(cap.get(3))
    height = int(cap.get(4))
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

    out = cv2.VideoWriter(str(testgui.filesave), fcc, fps, (width, height))

    hog=cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    lower_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
    upper_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

    while True:
        ret, frame = cap.read()
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayframe, 1.1, 2, 0, (20, 20))
        lower = lower_cascade.detectMultiScale(grayframe, 1.1, 2, 0, (20, 20))
        upper = upper_cascade.detectMultiScale(grayframe, 1.1, 2, 0, (20, 20))

        if not ret:
            break
    
        detected, _=hog.detectMultiScale(frame)

        for(x, y, w, h) in detected:
            body_img=frame[y:y+h,x:x+w]
            body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
            body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
            frame[y:y+h,x:x+w] = body_img

        for(x, y, w, h) in faces:
            body_img=frame[y:y+h,x:x+w]
            body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
            body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
            frame[y:y+h,x:x+w] = body_img

        for(x, y, w, h) in upper:
            body_img=frame[y:y+h,x:x+w]
            body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
            body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
            frame[y:y+h,x:x+w] = body_img

        for(x, y, w, h) in lower:
            body_img=frame[y:y+h,x:x+w]
            body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
            body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
            frame[y:y+h,x:x+w] = body_img
            
        cv2.imshow("Body", frame)
        out.write(frame)
        if cv2.waitKey(10) == 27:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
