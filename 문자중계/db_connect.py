import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='Odmc7721!!',
                     db='project_cn')

cursor = db.cursor()