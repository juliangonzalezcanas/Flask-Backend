from flask import Flask, request, jsonify
import pymysql


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Julixx26'
app.config['MYSQL_DB'] = 'clothing'

mysql = pymysql.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password= app.config['MYSQL_PASSWORD'],
    db = app.config['MYSQL_DB']
)

def create_table():
    try:
        print('Creating Table Started =====')
        cur = mysql.cursor()
        cur.execute(
            '''

                CREATE TABLE IF NOT EXISTS `clothing`.`user` (
                    `id` INT NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(45) NOT NULL,
                    `surname` VARCHAR(45) NOT NULL,
                    `adress` VARCHAR(45) NOT NULL,
                    `code` VARCHAR(45) NOT NULL,
                PRIMARY KEY (`id`))

            '''
        )
        mysql.commit()
        cur.close()
        print('Items Table Created =====')
    except Exception as e:
        print("Error while creating table",e)

    



if __name__ == '__main__':
    create_table()
    app.run(debug=True)