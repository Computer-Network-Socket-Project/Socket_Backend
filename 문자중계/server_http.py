from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# MySQL 데이터베이스 연결 설정
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': '',
    'raise_on_warnings': True
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)

    if request.method == 'GET':
        # 데이터베이스에서 채팅 기록 가져오기
        query = ("SELECT chat, chat_datetime FROM chatting")
        cursor.execute(query)
        chats = cursor.fetchall()

        cursor.close()
        cnx.close()

        return jsonify(chats)
    elif request.method == 'POST':
        # 데이터베이스에 채팅 기록 저장하기
        chat = request.form['chat']
        add_chat = ("INSERT INTO chatting "
                    "(chat) "
                    "VALUES (%s)")
        data_chat = (chat,)
        cursor.execute(add_chat, data_chat)
        cnx.commit()

        cursor.close()
        cnx.close()

        return 'OK'

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    emit('response', 'This is a response')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, allow_unsafe_werkzeug=True)
