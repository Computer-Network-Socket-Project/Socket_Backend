# -*- codking: utf-8 -*-

# relay.py

# 중계화면에 게시글 값들 보여주기(GET)

from db_connect import cur

# front의 home에서 게시글을 클릭시 title 전달되면서 받아야함
# title = input() # front에서 읽어와야함

sql = """SELECT * 
    FROM GAME_INFO 
    """
cur.execute(sql)
relay_rows = cur.fetchall() #List type로 저장됨: [{},{}, ...]

# print(relay_rows) # 값이 잘 들어갔는지 확인하는 코드