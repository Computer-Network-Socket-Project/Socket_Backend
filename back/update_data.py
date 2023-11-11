# -*- codking: utf-8 -*-

# update_data.py

# GAME_INFO에 있는 데이터를 업데이트하는 코드

from db_connect import cur, con

def update_data(game_name, team1_name, team1_score, team2_name, team2_score,sport_type,game_half,game_progress):
        try:
            sql = """
                UPDATE GAME_INFO AS t1
                JOIN (SELECT MAX(id) AS max_id FROM game_info) AS t2
                SET t1.game_name = '{game_name}',
                    t1.team1_name = '{team1_name}',
                    t1.team1_score = {team1_score},
                    t1.team2_name = '{team2_name}',
                    t1.team2_score = {team2_score},
                    t1.sport_type = {sport_type},
                    t1.game_half = {game_half},
                    t1.game_progress = {game_progress}
                WHERE t1.id = t2.max_id;
                """.format(game_name = game_name, team1_name = team1_name, team1_score = team1_score, 
                           team2_name = team2_name, team2_score = team2_score, sport_type = sport_type, 
                           game_half = game_half, game_progress = game_progress)
            cur.execute(sql)
            con.commit()
            return "Data update successfullt"
        except Exception as e:
              return f"Error: {str(e)}"
        
print(update_data("test1","test1",1,
            "test1",2,1,
            1,1)
)
