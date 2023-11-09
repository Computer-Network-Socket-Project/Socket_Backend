# -*- codking: utf-8 -*-

# half.py

# 전/후반전 관련 코드

from db_connect import con, cur

def update_half(title):
    try:
        sql = """
            UPDATE GAME_INFO
            SET game_half = 1
            WHERE game_name='{title}';
            """.format(title=title)
        cur.execute(sql)
        con.commit()
        return "Data update successfully."
    except Exception as e:
        return f"Error: {str(e)}"
