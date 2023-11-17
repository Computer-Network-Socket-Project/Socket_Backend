# -*- codking: utf-8 -*-
import socket
import json
import struct
import threading
from db_connect import con, cur

isTrue = False
def handle_client(client_socket, addr):
    global isTrue
    print(f'Connection from {addr} has been established!')

    while True:
        try:

            # 먼저 데이터의 길이를 읽습니다.
            data_length = client_socket.recv(4)
            if not data_length:
                break
            data_length = struct.unpack('<I', data_length)[0]

            # 그 다음 데이터의 길이만큼 데이터를 읽습니다.
            data = client_socket.recv(data_length)
            if not data:
                break
            data = data.decode()

            # JSON 파싱
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                print("Failed to parse JSON")
                continue

            # 클라이언트의 요청에 따라서 처리를 합니다.
            if data["type"] == "creater" and data["action"] == "update_request":
                print("나는 creater에요")
                # Creater의 요청을 처리합니다.
                # 데이터를 보내라는 신호를 보냅니다.
                response = {"type": "server", "action": "send_data"}
                response_json = json.dumps(response).encode('utf-8')
                response_length = struct.pack('<I', len(response_json))

                client_socket.send(response_length)
                client_socket.send(response_json)

            elif data["type"] == "creater" and data["action"] == "update_data":
                print("db 업데이트좀")
                # Creater로부터 받은 데이터를 DB에 업데이트합니다.
                game_data = {}
                game_data['game_name'] = data['game_name']
                game_data['team1_name'] = data['team1_name']
                game_data['team1_score'] = data['team1_score']
                game_data['team2_name'] = data['team2_name']
                game_data['team2_score'] = data['team2_score']
                game_data['sport_type'] = data['sport_type']
                game_data['game_half'] = data['game_half']
                game_data['game_progress'] = data['game_progress']
                print(f'game_data={game_data}')
                # DB 업데이트 코드
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
                        game_name = game_data['game_name'], team1_name = game_data['team1_name'], team1_score = game_data['team1_score'],
                        team2_name = game_data['team2_name'], team2_score = game_data['team2_score'], sport_type = game_data['sport_type'],
                        game_half = game_data['game_half'], game_progress = game_data['game_progress']
                        )
                cur.execute(sql)
                con.commit()
                data['viewer_on'] = 1
                print(f'data= {data}')
                isTrue = True

            if isTrue == 1 and data['viewer_on'] == 1:
                print("viewer 받아요")
                # Viewer의 요청을 처리합니다.
                # DB에서 필요한 데이터를 가져옵니다.
                # 필요시 DB 조회 코드 작성
                sql = """
                    SELECT * 
                    FROM GAME_INFO 
                    WHERE ID = (SELECT MAX(ID) FROM GAME_INFO);  
                    """
                cur.execute(sql)
                game_data = cur.fetchone()
                print(game_data)

                # 가져온 데이터를 Viewer에게 보냅니다.
                response = {"type": "server", "action": "send_data", 'game_name':game_data['game_name'], 'team1_name':game_data['team1_name'], 'team1_score':game_data['team1_score'], 'team2_name':game_data['team2_name'], 'team2_score':game_data['team2_score'], 'sport_type':game_data['sport_type'], 'game_half':game_data['game_half'], 'game_progress':game_data['game_progress']}
                print(response)
                response_json = json.dumps(response).encode('utf-8')
                response_length = struct.pack('<I', len(response_json))

                client_socket.send(response_length)
                client_socket.send(response_json)
                #data['viewer_on'] = 0
                isTrue = False

        except ConnectionResetError:
            break
    client_socket.close()

server_ip = '0.0.0.0'
server_port = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen()

while True:
    print("반복문 실행중")
    client_socket, addr = server_socket.accept()

    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()

