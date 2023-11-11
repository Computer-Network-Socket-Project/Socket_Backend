# -*- codking: utf-8 -*-

# select_data.py

# GAME_INFO에 있는 모든 데이터 읽어오는 코드

from db_connect import cur

def select_data():
    sql = "SELECT * FROM GAME_INFO;"
    cur.execute(sql)
    rows = cur.fetchall() #List type로 저장됨: [{},{}, ...]
    return rows

# print(rows) # 값이 잘 들어갔는지 확인하는 코드

"game_datetime","game_half","game_progress","game_name","great_num","id","sport_type","team1_name","team1_score","team2_name","team2_score"