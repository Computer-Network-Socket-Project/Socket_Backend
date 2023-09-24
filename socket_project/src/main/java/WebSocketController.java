import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;

@Controller
public class WebSocketController {

    @MessageMapping("/chat") // 클라이언트에서 메시지를 /app/chat 경로로 보낼 때 이 핸들러가 처리합니다.
    @SendTo("/topic/messages") // 이 경로로 메시지를 브로드캐스팅합니다.
    public Message sendMessage(Message message) {
        // 메시지 처리 로직을 작성합니다.
        return message;
    }
}
