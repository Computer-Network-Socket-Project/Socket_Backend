# -*- codking: utf-8 -*-

# home.py

# home화면에 게시글 값들 보여주기(GET)

from db_connect import cur

sql = "SELECT * FROM GAME_INFO;"
cur.execute(sql)
home_rows = cur.fetchall() #List type로 저장됨: [{},{}, ...]

# print(home_rows) # 값이 잘 들어갔는지 확인하는 코드