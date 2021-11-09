import pymysql
from PIL import Image
import numpy as np

#이미지 인수 넘겨 받으려면 수정 필요

def insertImg(tableName, image):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
                )

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
