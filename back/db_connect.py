# -*- codking: utf-8 -*-

# db_connect.py

# 데이터베이스 연결 및 커서 생성 코드

# STEP1. PyMySql 모듈을 import
import pymysql

# STEP2. MySQL 연결: pymysql.connect()
## 호스트명, 로그인, 암호, 접속할 DB 등 지정
host = "localhost"
user = "root"
password = "" # 사람마다 값이 다를 수 있습니다.(각자 변경 필요)
db = "" # 사람마다 값이 다를 수 있습니다.(각자 변경 필요)

con = pymysql.connect(host=host, user=user, password=password, 
                       db=db, charset='utf8', # 한글처리 (charset="utf-8")
                       autocommit=True, # 결과 DB 반영(Insert or Update)
                       cursorclass=pymysql.cursors.DictCursor # DB 조회시 컬럼명을 동시에 보여줌
                       ) 

# STEP3. DB커서 객체생성: Connection 객체로부터 cursor() 호출
cur = con.cursor()
