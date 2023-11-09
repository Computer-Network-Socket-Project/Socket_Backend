# -*- codking: utf-8 -*-

# like.py

# 좋아요 수 관련 코드

from db_connect import con,cur

def update_like(title):
    try:
        sql = """UPDATE GAME_INFO
            SET great_num = great_num + 1
            WHERE game_name='{title}';
            """.format(title=title)
        cur.execute(sql)
        con.commit()
        return "Data update successfully."
    except Exception as e:
        return f"Error: {str(e)}"