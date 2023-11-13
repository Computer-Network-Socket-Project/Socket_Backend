from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# MySQL 데이터베이스 연결 설정
config = {
    'user': 'root',
    'password': '',  # 적절한 비밀번호로 바꿔주세요.
    'host': 'localhost',
    'database': '',  # 적절한 데이터베이스 이름으로 바꿔주세요.
    'raise_on_warnings': True
}
#chat, data_chat db에서 받기
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)

    try:
        if request.method == 'GET':
            # 데이터베이스에서 채팅 기록 가져오기
            query = ("SELECT chat, chat_datetime FROM chatting ORDER BY chat_datetime")  # 채팅 시간 오름차순으로 정렬
            cursor.execute(query)
            chats = cursor.fetchall()

            return jsonify(chats)

        elif request.method == 'POST':
            # 데이터베이스에 채팅 기록 저장하기
            chat = request.json['chat']  # request.form 대신 request.json 사용
            chat_datetime = datetime.now()
            add_chat = ("INSERT INTO chatting "
                        "(chat, chat_datetime) "
                        "VALUES (%s, %s)")
            data_chat = (chat, chat_datetime)
            cursor.execute(add_chat, data_chat)
            cnx.commit()

            # 새로운 채팅 메시지와 시간을 JSON 형식으로 반환
            new_chat = {
                "chat": chat,
                "chat_datetime": chat_datetime.strftime("%a, %d %b %Y %H:%M:%S GMT")  # datetime 객체를 문자열로 변환
            }
            return jsonify(new_chat)

    except Exception as e:
        print("Error occurred:", e)
        return "Error occurred"

    finally:
        cursor.close()
        cnx.close()

    return 'OK'

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    emit('response', 'This is a response')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, allow_unsafe_werkzeug=True)
