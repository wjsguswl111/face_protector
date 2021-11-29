import pymysql
from PIL import Image
import numpy as np
import imageio


#값 저장하는 테이블 생성 함수
def creTable2():
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS members (memName VARCHAR(255), result VARCHAR(255))")

    finally:
        connection.commit()
        connection.close()

#값 저장하기 (이름, 값)
def saveResult(mem, re):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO members (memName, result) VALUES (%s, %s)"
        #re = str(re)
        val = (mem, re)
        cursor.execute(sql,val)

    finally:
        connection.commit()
        connection.close()

#값 불러오기(이름)
def callResult():
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM members")
        res = cursor.fetchall()

        mem = {}
        for x in res:
            mem[x[0]] = x[1]
            
        return mem

    finally:
        connection.commit()
        connection.close()

def creTable(tableName):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE "+ tableName +" (img MEDIUMTEXT, size VARCHAR(255))")

    finally:
        connection.commit()
        connection.close()

def delTable(tableName):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS " + tableName)

    finally:
        connection.commit()
        connection.close()

def imgToDB(tableName, image):
    #이미지 인수 넘겨 받으려면 수정 필요
    #img = Image.open("C:\choun1.jpg")
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    
    img_size = image.shape
    list_img = image.tolist()
    str_img = str(list_img)
    characters = "[],"
    for x in range(len(characters)):
        str_img = str_img.replace(characters[x],"")

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO "+tableName+" (img, size) VALUES (%s, %s)"
        val = (str_img, str(img_size))
        cursor.execute(sql,val)

    finally:
        connection.commit()
        connection.close()

def imgFromDB(tableName):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
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
        
            name = "image\\" + str(i) + ".jpeg"
        
            img2 = img.split()
            img2 = list(map(int, img2))
            img2 = np.array(img2).reshape((int(size[0]),int(size[1]),int(size[2])))
            imageio.imwrite(name, img2)


    finally:
        connection.close()

def showTable():
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        res = cursor.fetchall()
        tab = list()
        for x in res:
            characters = "(),'"
            x=str(x)
            for c in range(len(characters)):
                x = x.replace(characters[c],"")
            if x != "members" and x != "stars":
                tab.append(x)
        return tab

    finally:
        connection.commit()
        connection.close()
        
def showimg(tableName):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT img, size FROM " + tableName + " LIMIT 1")
        res = cursor.fetchall()
        for x in res:
            img=x[0]
            size=x[1]
        characters = "(),"
        for c in range(len(characters)):
            size = size.replace(characters[c],"")
        size = size.split()
        size = list(map(int, size))
        img2 = img.split()
        img2 = list(map(int, img2))
        img2 = np.array(img2).reshape((int(size[0]),int(size[1]),int(size[2])))
        return img2
        
            
    finally:
        connection.commit()
        connection.close()

def creStarTable():
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS stars (memName VARCHAR(255))")

    finally:
        connection.commit()
        connection.close()

def intoStar(star):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO stars (memName) VALUES (%s)"
        val = (star)
        cursor.execute(sql,val)

    finally:
        connection.commit()
        connection.close()