import cv2
import os
import cvlib as cv
from cvlib.object_detection import draw_bbox

cap = cv2.VideoCapture('C:/Users/wjsgu/Desktop/test.avi')

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    #frame = imutils.resize(frame, width=800, height=800)
    bbox, label, conf = cv.detect_common_objects(cap)

    print(bbox, label, conf)
    cap = draw_bbox(cap, bbox, label, conf)

    cv2.imshow("Detect", frame)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()