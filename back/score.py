# -*- codking: utf-8 -*-

# score.py

# 점수 관련 코드
from db_connect import cur,con

# def team_score(title):
#     try:
#         rows = [row
#                 for row in select_data()
#                 if row['game_name']==title]
#         # rows[0]["team_name"]
#         return rows[0]["team_name", "team_score"]
#     except Exception as e:
#         return f"Error: {str(e)}"

# print(team_score('title1'))

def update_score(title, score1, score2):
    try:
        sql = """UPDATE GAME_INFO
        SET team1_score = {score1} AND team2_score = {score2}
        WHERE game_name='{title}';
        """.format(title=title, score1=score1, score2=score2)
        cur.execute(sql)
        con.commit()
        return "Data update successfully."
    except Exception as e:
        return f"Error: {str(e)}"
    
update_score('test1', 1, 0)