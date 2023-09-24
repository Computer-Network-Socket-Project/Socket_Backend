import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;

@Controller
public class ScoreController {

    private final Score currentScore = new Score();

    @MessageMapping("/updateScore")
    @SendTo("/topic/scoreUpdates")
    public Score updateScore() {
        // 현재 점수 가져오기
        int current = currentScore.getValue();

        // 새로운 점수 계산 (예: 1 증가)
        int newScore = current + 1;

        // 새로운 점수 저장
        currentScore.setValue(newScore);

        // 점수를 브로드캐스팅하여 모든 클라이언트에게 업데이트된 점수 전송
        return currentScore;
    }
}
