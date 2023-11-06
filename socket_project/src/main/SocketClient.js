var socket = new SockJS('/ws'); // 서버의 WebSocket 엔드포인트에 연결
var stompClient = Stomp.over(socket);

stompClient.connect({}, function(frame) {
    // 연결 성공 시 처리 로직
});

// 메시지 수신을 처리하는 코드
stompClient.subscribe("/topic/messages", function(message) {
    // 메시지 처리 로직
});

// 메시지 전송 예시
stompClient.send("/app/chat", {}, JSON.stringify({ content: "Hello", sender: "User" }))