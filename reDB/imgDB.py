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
        cursor.execute("CREATE TABLE "+ tableName +" (name VARCHAR(255), img MEDIUMTEXT, size VARCHAR(255))")

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
    img = Image.open("C:\choun1.jpg")
    img_size = str(img.size)

    numpy_img = np.array(img)
    list_img = numpy_img.tolist()
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
        cursor.execute("SELECT name, img, size FROM " + tableName)
        res = cursor.fetchall()

        for x in res:
            name = x[0]
            img = x[1]
            size = x[2]

            characters = "(),"
            for x in range(len(characters)):
                size = size.replace(characters[x],"")
            size = size.split()
            size = list(map(int, size))
        
            name = name + ".jpeg"
        
            img2 = img.split()
            img2 = list(map(int, img2))
            img2 = np.array(img2).reshape((int(size[1]),int(size[0]),3))
            imageio.imwrite(name, img2)

    finally:
        connection.close()