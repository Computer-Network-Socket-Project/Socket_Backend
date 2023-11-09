# -*- codking: utf-8 -*-

# game_over.py

# 게임 종료시 진행상황(game_progress)을 0으로 바꿔주는 코드(1:진행/0:종료)

from db_connect import con, cur

# title = input() # front에서 받을 값

def update_game(title):
    try:
        sql = """UPDATE GAME_INFO
            SET game_progress = 0
            WHERE game_name='{title}';
            """.format(title=title)
        cur.execute(sql)

        con.commit()
        return "Data update successfully."
    except Exception as e:
        return f"Error: {str(e)}"

# # 값이 잘 들어갔나 확인하는 코드(확인용이므로 주석처리 또는 삭제할 예정)
# sql = """SELECT *
#     FROM GAME_INFO;
#     """
# cur.execute(sql)

# rows = cur.fetchall()
# print(rows)
