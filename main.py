import socket
from _thread import *
from datetime import datetime

HOST = '192.168.0.8'  # server IP 수시로 cheak
PORT = 8889

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 클라이언트 유형을 입력 받음
client_type = input("Enter client type ('relay' or 'viewer'): ")


def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)
        print("Received:", repr(data.decode()))


start_new_thread(recv_data, (client_socket,))
print('>> Connect Server')

while True:
    message = input()

    if message == 'quit':  # 생성 클라이언트가 문자 종료 중계하고 싶을 때
        break

    # 클라이언트 유형과 메시지를 서버로 전달
    message_with_type = f"{client_type}:{message} ({datetime.now().strftime('+ %Y-%m-%d %H:%M:%S')})"
    client_socket.send(message_with_type.encode())

client_socket.close()
