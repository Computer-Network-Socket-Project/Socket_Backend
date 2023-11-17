# -*- codking: utf-8 -*-
import socket
import json
import struct
import threading
from db_connect import con, cur

viewer_sockets = []
message_sockets = []
def handle_creater_request(data, client_socket):
    if data["action"] == "update_request":
        print("나는 creater에요")
        response = {"type": "server", "action": "send_data"}
        response_json = json.dumps(response).encode('utf-8')
        response_length = struct.pack('<I', len(response_json))

        client_socket.send(response_length)
        client_socket.send(response_json)

    elif data["action"] == "update_data":
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
            game_name=game_data['game_name'], team1_name=game_data['team1_name'], team1_score=game_data['team1_score'],
            team2_name=game_data['team2_name'], team2_score=game_data['team2_score'],
            sport_type=game_data['sport_type'],
            game_half=game_data['game_half'], game_progress=game_data['game_progress']
        )
        cur.execute(sql)
        con.commit()
        data['viewer_on'] = 1
        print(f'data= {data}')

        response = {"type": "server", "action": "send_data", 'game_name': game_data['game_name'],
                    'team1_name': game_data['team1_name'], 'team1_score': game_data['team1_score'],
                    'team2_name': game_data['team2_name'], 'team2_score': game_data['team2_score'],
                    'sport_type': game_data['sport_type'], 'game_half': game_data['game_half'],
                    'game_progress': game_data['game_progress']}
        print(response)
        response_json = json.dumps(response).encode('utf-8')
        response_length = struct.pack('<I', len(response_json))

        # 모든 viewer에게 데이터 전송
        for viewer_socket in viewer_sockets:
            viewer_socket.send(response_length)
            viewer_socket.send(response_json)

    # 문자중계 코드 추가
    elif data["action"] == "update_message":
        print("문자 중계")
        message = data["message"] 
        # DB 업뎃
        sql = """
                INSERT INTO chatting (game_name, chat)
                SELECT game_name, '{message}'
                FROM game_info
                WHERE id = (SELECT MAX(id) FROM game_info);
                """.format(message=message)
        cur.execute(sql)
        con.commit()
        print(f"massage_data = {data}")
        # 모든 viewer에게 데이터 전송
        for message_socket in message_sockets:
            message_socket.send(response_length)
            message_socket.send(response_json)

def handle_viewer_request(data, client_socket):
    if data["action"] == "data_request":
        print("viewer 받아요")
        # Viewer의 요청을 처리합니다.
        # DB에서 필요한 데이터를 가져옵니다.
        sql = """
                            SELECT * 
                            FROM GAME_INFO 
                            WHERE ID = (SELECT MAX(ID) FROM GAME_INFO);  
                            """
        cur.execute(sql)
        game_data = cur.fetchone()
        print(game_data)

        # 가져온 데이터를 Viewer에게 보냅니다.
        response = {"type": "server", "action": "send_data", 'game_name': game_data['game_name'],
                    'team1_name': game_data['team1_name'], 'team1_score': game_data['team1_score'],
                    'team2_name': game_data['team2_name'], 'team2_score': game_data['team2_score'],
                    'sport_type': game_data['sport_type'], 'game_half': game_data['game_half'],
                    'game_progress': game_data['game_progress']}
        print(response)
        response_json = json.dumps(response).encode('utf-8')
        response_length = struct.pack('<I', len(response_json))

        client_socket.send(response_length)
        client_socket.send(response_json)
        viewer_sockets.append(client_socket)
        # data['viewer_on'] = 0
        
    # 문자중계 서비스 데이터 받는 코드
    elif data["action"] == "message_request":
        print("viewer message 받아요")
        print("viewer 받아요")
        # Viewer의 요청을 처리합니다.
        # DB에서 필요한 데이터를 가져옵니다.
        sql = """
                SELECT * 
                FROM CHATTING 
                WHERE GAME_NAME = (SELECT GAME_NAME 
                                    FROM GAME_INFO 
                                    WHERE ID = (SELECT MAX(ID) FROM GAME_INFO));  
                """
        cur.execute(sql)
        message_data = cur.fetchall()
        print(message_data)
        # 가져온 데이터를 Viewer에게 보냅니다.
        response = {"type": "server", "action": "send_message",}
        print(response)
        response_json = json.dumps(response).encode('utf-8')
        response_length = struct.pack('<I', len(response_json))

        client_socket.send(response_length)
        client_socket.send(response_json)
        message_sockets.append(client_socket)


def handle_client(client_socket, addr):
    global isTrue
    print(f'Connection from {addr} has been established!')

    while True:
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

        if data["type"] == "creater":
            handle_creater_request(data, client_socket)
        elif data["type"] == "viewer":
            handle_viewer_request(data, client_socket)

server_ip = 'localhost'
server_port = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen()

while True:
    print("반복문 실행중")
    client_socket, addr = server_socket.accept()

    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()