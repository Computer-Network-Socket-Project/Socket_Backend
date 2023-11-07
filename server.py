import socket
import threading

# 서버의 IP 주소와 포트 번호를 설정합니다.
HOST = '0.0.0.0'
PORT = 12345  # 사용할 포트 번호

# 경기 생성자 클라이언트와 문자를 볼 수만 있는 클라이언트를 구분하기 위한 딕셔너리
clients = {}


# 클라이언트와 메시지를 중계하는 함수
def handle_client(client_socket):
    global client_id
    try:
        # 클라이언트의 ID를 받아옵니다.
        client_id = client_socket.recv(1024).decode()
        print(f"Connected: {client_id}")

        # 클라이언트를 저장하고, 메시지 중계를 위한 루프를 시작합니다.
        clients[client_id] = client_socket
        while True:
            message = client_socket.recv(1024).decode()
            if message:
                # 클라이언트가 종료를 요청한 경우
                if message == "exit":
                    client_socket.close()
                    del clients[client_id]
                    print(f"Disconnected: {client_id}")
                    break

                # 메시지를 모든 다른 클라이언트에게 중계합니다.
                for client_id, socket in clients.items():
                    if client_id != sender_id:
                        socket.send(message.encode())
    except Exception as e:
        print(f"Error: {str(e)}")
        client_socket.close()
        del clients[client_id]



# 서버 소켓을 생성하고 클라이언트의 연결을 기다립니다.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"Listening on {HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    # 클라이언트 ID를 받아옵니다. 경기 생성자인지 여부를 확인할 수 있도록 구분합니다.
    client_id = client_socket.recv(1024).decode()

    # 경기 생성자인 경우
    if client_id == "creator":
        creator_client = client_socket
        print("Creator connected")
    # 일반 클라이언트인 경우
    if client_id == "viewer":
        # 클라이언트를 볼 수만 있는 클라이언트로 구분합니다.
        print("Viewer connected")
        # 메시지 중계를 위한 스레드를 시작합니다.
        threading.Thread(target = handle_client, args = (client_socket, client_id)).start()
