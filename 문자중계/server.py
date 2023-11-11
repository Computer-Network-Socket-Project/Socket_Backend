import socket
from _thread import *
from datetime import datetime

client_sockets = []

## Server IP and Port ##

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999


########## processing in thread ##
## new client, new thread ##

def threaded(client_socket, addr):
    print('>> Connected by:', addr[0], ':', addr[1])

    ## process until client disconnect ##
    while True:
        try:
            ## send client if data received(echo) 최대 1024바이트까지 가능. (버퍼 크기)
            data = client_socket.recv(1024)

            if not data:
                print('>> Disconnected by', addr[0], ':', addr[1])
                break

            client_type = data.decode().split(':')[0]  # 클라이언트 유형을 ':'로 구분
            chat = data.decode().split(':', 1)[1]  # ':'로 구분된 첫 번째 ':' 이후의 내용은 메시지

            if client_type == 'viewer':
                # 중계 메시지를 입력하는 클라이언트의 경우 다른 중계 클라이언트에게 메시지 전달
                for client in client_sockets:
                    if client != client_socket and 'relay' in client.recv(1024).decode():
                        client.send(chat.encode())
            elif client_type == 'relay':
                # 그냥 메시지를 받아보는 클라이언트의 경우 메시지 출력
                print('>> Received from', addr[0], ':', addr[1], chat)

            ## chat to client connecting client ##
            ## chat to client connecting client except person sending message ##
            for client in client_sockets:
                if client != client_socket:
                    message_with_time = f"{chat} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"
                    client.send(message_with_time.encode())

        except ConnectionResetError as e:
            print('>> Disconnected by', addr[0], ':', addr[1])
            break

    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print('remove client list:', len(client_sockets))

    client_socket.close()


############# Create Socket and Bind ##

print('>> Server Start with ip:', HOST)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

############# Client Socket Accept ##

try:
    while True:
        print('>> Wait')

        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        print("참가자 수:", len(client_sockets))  # 클라이언트 수 확인
except Exception as e:
    print('에러:', e)

finally:
    server_socket.close()
