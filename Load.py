import cv2
import os

str1 = input("name : ")

path = 'C:/Users/wjsgu/Desktop'
filePath = os.path.join(path, str1)

if os.path.isfile(filePath):
    cap = cv2.VideoCapture(filePath)
else:
    print("file load failed!")

frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_size = (frameWidth, frameHeight)
print('frame_size={}'.format(frame_size))

frameRate = 33

while True:
    ret, frame = cap.read()
    if not(ret):
        break
    
    cv2.imshow('video', frame)
    key = cv2.waitKey(frameRate)

    if key == 27:
        break

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()