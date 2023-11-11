## SERVER ##

import socket
from _thread import *

client_sockets = []
client_types = {}  # 각 클라이언트의 타입을 저장하는 딕셔너리 추가

## Server IP and Port ##

HOST = '0.0.0.0'  # 모든 사용 가능한 네트워크 인터페이스를 의미
PORT = 9999


########## processing in thread ##
## new client, new thread ##

def threaded(client_socket, addr):
    print('>> Connected by :', addr[0], ':', addr[1])

    ## process until client disconnect ##
    while True:
        try:
            ## send client if data recieved(echo) ##
            data = client_socket.recv(1024)

            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

            message = data.decode().split(':', 1)[1]  # ':'로 구분된 첫 번째 ':' 이후의 내용은 메시지

            if client_types[client_socket]:  # 딕셔너리에서 클라이언트 소켓을 키로 사용
                # 중계 메시지를 입력하는 클라이언트의 경우 다른 중계 클라이언트에게 메시지 전달
                for client in client_sockets:
                    if client != client_socket and 'relay' in client.recv(1024).decode():
                        client.send(message.encode())

                # 채팅 메시지와 시간을 데이터베이스에 저장
                sql = "INSERT INTO chatting (chat, chat_datetime) VALUES (%s, NOW())"
                cursor.execute(sql, (message,))  # 쿼리 실행
                db.commit()  # 변경 사항 커밋
            else:
                # 그냥 메시지를 받아보는 클라이언트의 경우 메시지 출력
                print('>> Received from ' + addr[0], ':', addr[1], message)

            ## chat to client connecting client ##
            ## chat to client connecting client except person sending message ##
            for client in client_sockets:
                if client != client_socket:
                    client.send(data)

        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print('remove client list : ', len(client_sockets))

    client_socket.close()


############# Create Socket and Bind ##

print('>> Server Start with ip :', HOST)
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
        client_type = bool(int(input("Enter client type (1 for 방 생성자, 0 for 경기 관람): ")))  # 클라이언트 타입 입력 받기
        client_types[client_socket] = client_type  # 딕셔너리에 클라이언트 소켓과 타입 저장
        start_new_thread(threaded, (client_socket, addr))
        print("참가자 수 : ", len(client_sockets))  # 클라이언트 수 확
except Exception as e:
    print('에러 : ', e)

finally:
    server_socket.close()
