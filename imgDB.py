import pymysql
from PIL import Image
import numpy as np
import imageio

connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )

def creTable(tableName):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE "+ tableName +" (img MEDIUMTEXT, size VARCHAR(255))")

    finally:
        connection.commit()
        connection.close()

def delTable(tableName):
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS " + tableName)

    finally:
        connection.commit()
        connection.close()

def imgToDB(tableName, image):
    #이미지 인수 넘겨 받으려면 수정 필요
    #img = Image.open("C:\choun1.jpg")
    img_size = image.shape

    list_img = image.tolist()
    str_img = str(list_img)
    characters = "[],"
    for x in range(len(characters)):
        str_img = str_img.replace(characters[x],"")

    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO "+tableName+" (name, img, size) VALUES (%s, %s, %s)",("chosun1", str_img, img_size)) #이미지이름도 변경필요, 없애던가

    finally:
        connection.commit()
        connection.close()

def imgFromDB(tableName):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT img, size FROM " + tableName)
        res = cursor.fetchall()
        
        i=0
        
        for x in res:
            img = x[0]
            size = x[1]
            i = i+1
            
            characters = "(),"
            for c in range(len(characters)):
                size = size.replace(characters[c],"")
            size = size.split()
            size = list(map(int, size))
        
            name = str(i) + ".jpeg"
        
            img2 = img.split()
            img2 = list(map(int, img2))
            img2 = np.array(img2).reshape((int(size[0]),int(size[1]),int(size[2])))
            imageio.imwrite(name, img2)

    finally:
        connection.close()