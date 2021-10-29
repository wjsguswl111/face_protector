import cv2
import imutils

cap = cv2.VideoCapture('C:/Users/wjsgu/Desktop/test.avi') #비디오 파일 불러오기
font = cv2.FONT_HERSHEY_SIMPLEX #사람 감지 글씨체 정의

cv2.namedWindow('Face')

face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
lower_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
upper_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')


while(True):
    ret, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayframe, 1.1, 2, 0, (30, 30))
    #lower = lower_cascade.detectMultiScale(grayframe, 1.8, 2, 0, (30, 30))
    #upper = upper_cascade.detectMultiScale(grayframe, 1.8, 2, 0, (30, 30))
    #frame = imutils.resize(frame, width=1000, height=1000)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3, 4, 0)
        cv2.putText(frame, 'Detected human', (x-5, y-5), font, 0.9, (255,255,0),2)

    '''for (x,y,w,h) in lower:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3, 4, 0)
        cv2.putText(frame, 'Detected human', (x-5, y-5), font, 0.9, (255,255,0),2)

    for (x,y,w,h) in upper:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3, 4, 0)
        cv2.putText(frame, 'Detected human', (x-5, y-5), font, 0.9, (255,255,0),2)'''
   
    cv2.imshow('Face',frame)

    if cv2.waitKey(10) == 27:
        break

cap.release()

cv2.destroyWindow('Face')

