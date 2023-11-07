from db_connect import con, cur

title = input() # front에서 받을 값
sql = """UPDATE GAME_INFO
    SET game_progress = 0
    WHERE game_name='{title}';
    """.format(title=title)
cur.execute(sql)

con.commit()

sql = """SELECT *
    FROM GAME_INFO;
    """
cur.execute(sql)

rows = cur.fetchall()
print(rows)
