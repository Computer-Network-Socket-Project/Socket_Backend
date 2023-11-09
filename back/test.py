from db_connect import cur,con

title = input()

sql = """
SELECT team_name,team_score
FROM GAME_INFO
WHERE game_name = '{title}' 
""".format(title=title)
cur.execute(sql)
rows = cur.fetchall()
print(rows)
print("-----------")
print(rows[0])
print(rows[1])
print("-----------")
print(list(dict(rows[0]).values()))
print(list(dict(rows[0]).values()))
print("-----------")
team2, score2 = list(dict(rows[1]).values())
team1, score1 = list(dict(rows[0]).values())
print( team1, team2, score1, score2)