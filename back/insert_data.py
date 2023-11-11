# -*- codking: utf-8 -*-

# insert_data.py

# 게시글 등록시 db에 값이 넣어지는 코드

from db_connect import con, cur
  
def insert_game(title):
	try:
		delete_sql = """
					delete from GAME_INFO 
					where game_name="새로운 게임이 진행할 예정입니다";
					"""
		cur.execute(delete_sql)
		con.commit()
		insert_sql = """INSERT INTO GAME_INFO (game_name) 
					VALUE ('{title}');
					""".format(title=title)
		cur.execute(insert_sql)
		con.commit()
		return "Data inserted successfully."
	except Exception as e:
		return f"Error: {str(e)}"

# process_data('title6')