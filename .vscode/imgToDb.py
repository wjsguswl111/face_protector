import pymysql
from PIL import Image
import numpy as np


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
    cursor.execute("INSERT INTO members (name, img, size) VALUES (%s, %s, %s)",("chosun1", str_img, img_size))

finally:
    connection.commit()
    connection.close()
