import imgDB
from PIL import Image
import numpy as np
import pymysql
import imageio

'''imgDB.creTable("joo")
img = Image.open("C:\chosun.jpg")
img = np.array(img)
imgDB.imgToDB("joo", img)
img = Image.open("C:\choun1.jpg")
img = np.array(img)
imgDB.imgToDB("joo", img)

imgDB.imgFromDB("joo")
'''
imgDB.creTable("ss")
img = Image.open("C:\choun3.jpg")
img = np.array(img)
imgDB.imgToDB("ss",img)
img = Image.open("C:\choun2.jpg")
img = np.array(img)
imgDB.imgToDB("ss",img)