import cv2

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_classifier1 = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
face_classifier2 = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
face_classifier3 = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
face_classifier4 = cv2.CascadeClassifier('haarcascade_profileface.xml')

cam = cv2.VideoCapture("dark.mp4")

a = 1

cv2.namedWindow('Face')

while True:
    img, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray, 1.1, 1)
    
    #cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]])
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)

    #faces4 = face_classifier4.detectMultiScale(gray, 1.0, 3)
    #for (x,y,w,h) in faces:
    #    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)

    frame = cv2.resize(frame,(int(frame.shape[1]*a), int(frame.shape[0]*a)))

    cv2.imshow('Face',frame)
    if cv2.waitKey(1)==27:
        break

cam.release()
cv2.destroyAllWindows()