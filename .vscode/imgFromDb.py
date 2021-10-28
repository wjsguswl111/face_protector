import pymysql
import numpy as np
from PIL import Image

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
        print(name)
        print("size type: ",type(size))

        characters = "(),"
        for x in range(len(characters)):
            size = size.replace(characters[x],"")
        size = size.split()
        size = list(map(int,size))
        print(size)
        
        img = img.split()
        img = list(map(int,img))
        img=np.array(img).reshape((size[1],size[0],3))
    
    img2 = Image.fromarray(img, 'RGB')
    img2.show()


finally:
    connection.close()
