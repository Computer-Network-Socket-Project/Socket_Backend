# -*- codking: utf-8 -*-
import socket
import json
import struct
from db_connect import con, cur

# 서버의 IP 주소와 포트 번호를 설정합니다.
server_ip = 'localhost'
server_port = 8080

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
            # 데이터를 저장만 할지, 보내야 할지
            isHaveToSend = False

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

            # 클라에서 서버로 보내달라고 요청이 온 경우
            if data == "receive_request":
                isHaveToSend = True



            print(f'Received data: {data}')

            # 소켓통신으로 바로 DB에 저장하는 코드
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

            # 데이터를 처리한 후 클라이언트에게 응답을 보냅니다.
            response = {
                # 'type': 'match_info',  # 응답 타입
                'game_name' : data['game_name'],
                'team1_name' : data['team1_name'],
                'team1_score' : data['team1_score'],
                'team2_name' : data['team2_name'],
                'team2_score' : data['team2_score'],
                'sport_type' : data['sport_type'],
                'game_half' : data['game_half'],
                'game_progress' : data['game_progress']

            }
            response_json = json.dumps(response)
            response_data = response_json.encode('utf-8')
            response_length = struct.pack('<I', len(response_data))  # 데이터 길이를 4바이트로 변환

            client_socket.send(response_length)  # 먼저 데이터 길이를 보냅니다.
            client_socket.send(response_data)  # 그 다음 데이터를 보냅니다.

        except ConnectionResetError:
            break

    client_socket.close()