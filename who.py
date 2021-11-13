#import fine_face as ff
import imutils
#from reDB import imgDB
import cv2

protoPath = "deploy.prototxt"
modelPath = "res10_300x300_ssd_iter_140000.caffemodel"
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

face = cv2.imread('test.jpg')
frame = imutils.resize(face, width=600)

#blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

cr = frame[200:400, 100:300]
print(type(cr))
cv2.imshow("cropped", cr)
cv2.waitKey(0)
#print(type(cr))
#imgDB.creTable("person")
#imgDB.imgToDB("person", blob)

#imgDB.imgFromDB("person")