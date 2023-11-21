# -*- codking: utf-8 -*-

# front_connect_test.py

# [andorid(kotlin)+flask] flask rest api 서버를 만들고 android retrofit2로 서버에서 데이터 가져오기

from flask import Flask, jsonify, request

from select_data import select_data
from insert_data import insert_game
from update_data import update_data
from like import update_like


app = Flask(__name__)

# HOME화면 모든 게임 정보 보여지는 부분
@app.route("/test1", methods=["GET", "POST"])
def home():
      # 좋아요 버튼 클릭시 작동하도록
      if request.method == "POST":
            data = request.get_json()
            title = data["game_name"]
            update_like(title)
      result = select_data()
      return jsonify(result)

# HOME에서 특정 게임을 선택한 후 보여지는 중계 화면에서 유저가 봐야하는 정보 부분
@app.route("/test2/<title>",methods=["GET"])
def relay(title):
      rows = select_data()
      result = [row 
                for row in rows 
                if row['game_name']==title]
      return jsonify(result)


@app.route("/test3",methods=["GET", "POST"])
def post():
      # HOME에서 +버튼을 누른 후 새로운 게시글을 등록할 때 보여지는 부분
      if request.method == "GET":
            title = "새로운 게임이 진행할 예정입니다"
            result = insert_game(title)
            return result
      # data update : update 버튼 혹은 뒤로가기 버튼을 누를 경우 발생함
      else:
            data = request.get_json()
            game_name = data["game_name"]
            team1_name = data["team1_name"]
            team1_score = data["team1_score"]
            team2_name = data["team2_name"]
            team2_score = data["team2_score"]
            sport_type = data["sport_type"]
            game_half = data["game_half"]
            game_progress = data["game_progress"]
            result = update_data(game_name, team1_name, team1_score, 
                              team2_name, team2_score,sport_type,
                              game_half,game_progress)
            return result


if __name__ == '__main__':
    app.run(host="192.168.0.7", port=8889, debug=True)