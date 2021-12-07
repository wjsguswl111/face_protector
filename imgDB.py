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

#값만 불러오기
def callResult2(name):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT result FROM members WHERE memName =(%s)",(name))
        res = cursor.fetchall()
        res = list(res)
        res = str(res[0])
        characters = "(),"
        for c in range(len(characters)):
            res = res.replace(characters[c],"")
        return res

    finally:
        connection.commit()
        connection.close()
        

#요소지우기
def delMember(name):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM members WHERE memName =(%s)",(name))

    finally:
        connection.commit()
        connection.close()
'''
def upResult(mem,re):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE members SET result = %s WHERE memName = %s",(re, mem))
        res = cursor.fetchall()

    finally:
        connection.commit()
        connection.close()
'''

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

#첫번째 이미지만 띄울때 사용  
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

#즐겨찾기 테이블 만드는것
def creStarTable():
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS stars (memName VARCHAR(255), result VARCHAR(255))")
        cursor.execute("ALTER TABLE stars ADD UNIQUE INDEX (memName)")

    finally:
        connection.commit()
        connection.close()


def intoStar(star,result):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        sql = "INSERT IGNORE INTO stars (memName, result) VALUES (%s,%s)"
        val = (star,result)
        cursor.execute(sql,val)

    finally:
        connection.commit()
        connection.close()

#즐겨찾기로부터 이름 가져오는것
def fromStar():
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT memName FROM stars")
        res = cursor.fetchall()

        li = []
        for x in res:
            characters = "(),'"
            for c in range(len(characters)):
                x =str(x).replace(characters[c],"")
            li.append(x)
        return li

    finally:
        connection.commit()
        connection.close()

#테이블 이름 바꾸기
def rename(old,new):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("ALTER TABLE "+old+" RENAME "+new)

    finally:
        connection.commit()
        connection.close()

#스타테이블에 저장된 이름 바꾸기
def reStar(old,new):
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE stars SET memName = %s WHERE memName = %s",(new,old))
        ####경로이름바꾸기##################################################

    finally:
        connection.commit()
        connection.close()

#멤버비우는 함수
def cleanMember():
    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )
    try:
        cursor = connection.cursor()
        cursor.execute("TRUNCATE members")

    finally:
        connection.commit()
        connection.close()
 #모자이크 다 끝나고 members 다 비우기
 #즐겨찾기ㅣ 할사람빼고 파일 다지우기yml
 #stars에 경로 저장할 곳 추가 ##
 #yml 파일 라내암