import pymysql

#각자 mysql에 따라 작성
db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     db='')

cursor = db.cursor()