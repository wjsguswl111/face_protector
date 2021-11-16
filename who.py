import numpy as np
import cv2
import imutils
from PIL import ImageGrab, Image
from pymysql import connect
import imgDB
import deleteFile
import fine_face as ff

def who_are():
    #얼굴 검출
            roi = ff.frame[ff.startY:ff.endY, ff.startX:ff.endX]
            roi = cv2.resize(roi, (200, 200))
            ro = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            result = ff.model.predict(roi)

            while(True):
                ff.cur.execute("SELECT * FROM members")
                ff.row = ff.cur.fetchone()
                if ff.row==None:
                    break
                if(result == ff.row[1]):
                    imgDB.imgToDB(ff.row[0], roi)
                else:
                    ff.name+=1
                    imgDB.creTable(str(ff.name))
                    imgDB.imgToDB(str(ff.name), roi)
                    imgDB.imgFromDB(str(ff.name))