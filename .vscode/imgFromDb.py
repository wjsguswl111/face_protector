import pymysql
import numpy as np
import imageio
#from PIL import Image

connection = pymysql.connect(
                host = '127.0.0.1',
                database = 'chosun',
                user = 'root',
                password = 'a5214645'
            )  
try:
    cursor = connection.cursor()
    cursor.execute("SELECT name, img, size FROM members")
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
