import os
import cv2

path=os.path.join('video','C:/Users/wjsgu/Desktop/test.avi')

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(path)
while True:
    ret, frame = cap.read()

    if not ret:
        break

    detected, _=hog.detectMultiScale(frame)

    for(x, y, w, h) in detected:
        cv2.rectangle(frame, (x, y, w, h), (0, 255, 0), 3)

    cv2.imshow("Detect", frame)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()