from db_connect import con, cur


# 게시글 생성시 디비 저장
title = input() # front에서 받을 값
team1 = input() # front에서 받을 값
team2 = input() # front에서 받을 값

# # 제약조건으로 코드 꼬여서 적음(주석처리 또는 삭제할 예정)
# # : test시 title명이 겹쳐서 생기는 에러를 방지하기 위한 코드(여기서 title은 pk로 값이 중복 없이 유일해야함)
# sql = "delete from GAME_INFO where game_name = '{title}';".format(title=title)
# cur.execute(sql)
# con.commit()
# sql = "delete from CHATTING where game_name = '{title}';".format(title=title)
# cur.execute(sql)
# con.commit()


sql = """INSERT INTO GAME_INFO (game_name, sport_type, team_name, game_progress) VALUES 
	('{title}', 0, '{team1}', 1),
	('{title}', 0, '{team2}', 1);
    """.format(title=title, team1=team1, team2=team2)
cur.execute(sql)

con.commit()

# # 값이 잘 들어갔나 확인하는 코드(확인용이므로 주석처리 또는 삭제할 예정)
# sql = "SELECT * FROM GAME_INFO;"
# cur.execute(sql)
# rows = cur.fetchall()
# print(rows)
# print(rows[:]['game_name'=="title1"]) # 이런식으로도 where구문 적용 가능 # 특정한 값을 검색할때 사용하는 코드