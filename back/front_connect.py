# -*- codking: utf-8 -*-

# front_connect_test.py

# [andorid(kotlin)+flask] flask rest api 서버를 만들고 android retrofit2로 서버에서 데이터 가져오기

from flask import Flask, jsonify, request

from select_data import select_data
from post import process_data
from game_over import update_game
from half import update_half
from like import update_like
from score import update_score

app = Flask(__name__)

# HOME화면 모든 게임 정보 보여지는 부분
@app.route("/test1", methods=["GET"])
def home():
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

# HOME에서 +버튼을 누른 후 새로운 게시글을 등록할 때 보여지는 부분
@app.route("/test3",methods=["POST"])
def post():
      data = request.get_json()
      title = data["game_name"]
      team1 = data["team1"]
      team2 = data["team2"]
      sport_type = data["sport_type"]
      if sport_type == "축구":
            sport_type = 0
      else:
            sport_type = 1
      result = process_data(title,team1,team2,sport_type)
      return result


# 게임 종료 버튼 누름 (**의논 필요**)
## 게임 정보도 불러오도록 GET방식도 추가하기
## => POST만 사용해도 괜찮을 것 같음 
## (: 종료시에는 game_name만 입력하고 종료버튼 누르면 끝이므로)
@app.route("/test4", methods=["POST"])
def game_over():
      data = request.get_json()
      title = data["game_name"]
      result = update_game(title)
      return result

# 전반전 -> 후반전 (**의논 필요** : 위와 같은 이유)
@app.route("/test5", methods=["POST"])
def half():
      data = request.get_json()
      title = data["game_name"]
      result = update_half(title)
      return result

# 좋아요 버튼 클릭시 작동하도록
@app.route("/test6", methods=["Post"])
def like():
      data = request.get_json()
      title = data["game_name"]
      result = update_like(title)
      return result

# 점수 수정시 작동하도록
@app.route("/test7/<title>", methods=["POST"])
def score(title):
      data = request.get_json()
      score1 = data["team1_score"]
      score2 = data["team2_score"]
      result = update_score(title, score1, score2)
      return result


if __name__ == '__main__':
    app.run(host="localhost", port=9999, debug=True)