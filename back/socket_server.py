# -*- codking: utf-8 -*-

# server.py
import socket
import json
from db_connect import con,cur

# 서버의 IP 주소와 포트 번호를 설정합니다.
server_ip = 'localhost'
server_port = 12345

# 소켓 객체를 생성하고, IP와 포트를 바인드합니다.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

# 클라이언트의 연결 요청을 기다립니다.
server_socket.listen()

while True:
    # 클라이언트의 연결 요청을 수락합니다.
    client_socket, addr = server_socket.accept()
    print(f'Connection from {addr} has been established!')

    while True:
        try:
            # 클라이언트로부터 데이터를 받습니다.
            data = client_socket.recv(1024)
            if not data: 
                break
            print(f'Received data: {data.decode()}')
            
            # 화면2에 데이터를 전송합니다.
            client_socket.send(data)

            # 소켓통신으로 바로 DB에 저장하는 코드
            # print(type(data.decode()))
            data = json.loads(data.decode())
            # print(data, type(data))
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
                """.format(
                        game_name = data['game_name'], team1_name = data['team1_name'], team1_score = data['team1_score'], 
                        team2_name = data['team2_name'], team2_score = data['team2_score'], sport_type = data['sport_type'], 
                        game_half = data['game_half'], game_progress = data['game_progress']
                        )
            cur.execute(sql)
            con.commit()

        except ConnectionResetError:
            break

    client_socket.close()
