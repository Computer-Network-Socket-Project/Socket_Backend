# client.py
import socket
import json

# 서버의 IP 주소와 포트 번호를 설정합니다.
server_ip = '192.168.0.13'
server_port = 8888

# 소켓 객체를 생성합니다.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결 요청을 보냅니다.
client_socket.connect((server_ip, server_port))

while True:
    # 서버에 데이터를 전송합니다.
    game_name = input("game_name: ")
    team1_name = input("team1_name: ")
    team2_name = input("team2_name: ")
    team1_score = int(input("team1_score: "))
    team2_score = int(input("team2_score: "))
    sport_type = int(input('sport_type: '))
    game_half = int(input('game_half: '))
    game_progress = int(input('game_progress: '))

    data = {"game_name": game_name,   
            "team1_name": team1_name, "team2_name": team2_name, 
            "team1_score": team1_score, "team2_score": team2_score,
            "sport_type": sport_type, "game_half": game_half, "game_progress": game_progress}
    client_socket.send(json.dumps(data).encode())

    # 서버로부터 데이터를 받습니다.
    data = client_socket.recv(1024)
    print(f'Received data: {data.decode()}')

    # 연결 종료 여부를 묻습니다.
    end_connection = input("Do you want to end the connection? (yes/no): ")
    if end_connection.lower() == 'yes':
        break

client_socket.close()
