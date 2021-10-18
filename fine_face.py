import cv2

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture("vfile.mp4")

a = 1


cv2.namedWindow('Face')



while True:
    img, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray,1.1,3)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    frame = cv2.resize(frame,(int(frame.shape[1]*a), int(frame.shape[0]*a)))

    cv2.imshow('Face',frame)
    if cv2.waitKey(1)==27:
        break

cam.release()
cv2.destroyAllWindows()