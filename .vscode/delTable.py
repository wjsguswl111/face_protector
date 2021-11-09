import pymysql

def delete(tableName):

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