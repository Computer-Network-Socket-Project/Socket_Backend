# -*- codking: utf-8 -*-

# score.py

# 점수 관련 코드
from db_connect import cur,con

def team_score(title):
    try:
        sql = """
        SELECT team_name,team_score
        FROM GAME_INFO
        WHERE game_name = '{title} 
        """.format(title=title)
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        return f"Error: {str(e)}"
 
def update_score(title, team, score):
    try:
        sql = """UPDATE GAME_INFO
        SET team_score = {score}
        WHERE game_name='{title}' and team_name='{team}';
        """.format(title=title,team=team, score=score)
        cur.execute(sql)

        con.commit()
        return "Data update suuccessfully."
    except Exception as e:
        return f"Error: {str(e)}"