import socket
import threading

# 클라이언트 소켓을 생성합니다.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버의 IP 주소와 포트 번호를 설정합니다.
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12345

# 클라이언트의 ID를 설정합니다.
client_id = "creator"  # 이 값을 "viewer"로 변경하여 볼 수만 있는 클라이언트로 사용 가능

# 서버에 연결합니다.    연결이 잘 안되면 host, port부분 오류일 수 있으니 잘 확인.
client_socket.connect((SERVER_HOST, SERVER_PORT))
client_socket.send(client_id.encode())

# 메시지를 보내는 함수
def send_message():
    while True:
        message = input("메시지를 입력하세요: ")
        client_socket.send(message.encode())

# 메시지를 받는 함수
def receive_message():
    while True:
        message = client_socket.recv(1024).decode() #server와 동일하게 값 설정
        print("수신: " + message)

def exit_chat():
    message = "exit"
    client_socket.send(message.encode())
    client_socket.close()

# 메시지를 보내는 스레드 시작
send_thread = threading.Thread(target=send_message)
send_thread.daemon = True
send_thread.start()

# 메시지를 받는 스레드 시작
receive_thread = threading.Thread(target=receive_message)
receive_thread.daemon = True
receive_thread.start()

# 클라이언트를 계속 실행
while True:
    pass
