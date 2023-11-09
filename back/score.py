# -*- codking: utf-8 -*-

# score.py

# 점수 관련 코드
from db_connect import cur,con
from select_data import select_data

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

def update_score(title, team, score):
    try:
        sql = """UPDATE GAME_INFO
        SET team_score = {score}
        WHERE game_name='{title}' and team_name='{team}';
        """.format(title=title,team=team, score=score)
        cur.execute(sql)
        con.commit()
        return "Data update successfully."
    except Exception as e:
        return f"Error: {str(e)}"