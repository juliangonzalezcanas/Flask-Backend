import pymysql
from app import mysql

def create_table():
    try:
        print('Creating Table Started =====')
        cur = mysql.cursor()
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY ,
                name VARCHAR(255) NOT NULL,
                description TEXT
            )
            '''
        )
        mysql.commit()
        cur.close()
        print('Items Table Created =====')
    except Exception as e:
        print("Error while creating table",e)
