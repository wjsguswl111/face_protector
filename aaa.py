import pymysql
connection = pymysql.connect(
                host = '127.0.0.1',
                database = 'chosun',
                user = 'root',
                password = 'a5214645'
        )
try:
    cursor = connection.cursor()
    cursor.execute("DELETE FROM members WHERE memName = n1")

finally:
    connection.commit()
    connection.close()