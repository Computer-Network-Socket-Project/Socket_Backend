# -*- codking: utf-8 -*-

# front_connect_test.py

# [andorid(kotlin)+flask] flask rest api 서버를 만들고 android retrofit2로 서버에서 데이터 가져오기

from flask import Flask, jsonify, request
from db_connect import con, cur
from home import home_rows
from relay import relay_rows
from post import process_data
from game_over import update_data
from half import update_half


app = Flask(__name__)

# HOME화면 모든 게임 정보 보여지는 부분
@app.route("/test1", methods=["GET"])
def home():
      return home_rows

# HOME에서 특정 게임을 선택한 후 보여지는 중계 화면에서 유저가 봐야하는 정보 부분
@app.route("/test2/<title>",methods=["GET"])
def relay(title):
      result = [row 
                for row in relay_rows 
                if row['game_name']==title]
      return jsonify(result)

# HOME에서 +버튼을 누른 후 새로운 게시글을 등록할 때 보여지는 부분
## front 연결 후 확인해야함: post방식이라 확인 불가
@app.route("/test3",methods=["POST"])
def post():
      title = request.form.get("game_name")
      team1 = request.form.get("team1")
      team2 = request.form.get("team2")
        
      result = process_data(title,team1,team2)
      return jsonify(result)

# 게임 종료 버튼 누름 (**의논 필요**)
## 게임 정보도 불러오도록 GET방식도 추가하기
## => POST만 사용해도 괜찮을 것 같음 
## (: 종료시에는 game_name만 입력하고 종료버튼 누르면 끝이므로)
@app.route("/test4", methods=["POST"])
def game_over():
      title = request.form.get("game_name")
      result = update_data(title)
      return jsonify(result)

# 전반전 -> 후반전 (**의논 필요** : 위와 같은 이유)
@app.route("/test5", methods=["GET","POST"])
def half():
      # if request.method == "POST":
            title = request.form.get("game_name")
            result = update_half(title)
            return jsonify(result)
      # else:
      #       result = [row 
      #             for row in relay_rows 
      #             if row['game_name']==title]
      #       return jsonify(result)



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5050, debug=True)