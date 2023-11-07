import socket
from _thread import *

HOST = ''  # 서버의 IP 주소 입력 연결 마다 HOST 값 맞게 작성하는 법 미완성.
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 클라이언트 유형을 입력 받음
client_type = input("Enter client type ('relay' or 'viewer'): ")

def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)
        print("Received: " + repr(data.decode()))

start_new_thread(recv_data, (client_socket,))
print('>> Connect Server')

while True:
    message = input()

    if message == 'quit':
        break

    # 클라이언트 유형과 메시지를 서버로 전달
    message_with_type = f"{client_type}:{message}"
    client_socket.send(message_with_type.encode())

client_socket.close()
