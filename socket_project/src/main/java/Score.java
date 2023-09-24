import lombok.Getter;

@Getter
public class Score {
    
    // 현재 점수를 반환
    private int value; // 점수를 나타내는 필드

    public Score() {
        this.value = 0; // 초기 점수를 0으로 설정
    }

    public void setValue(int value) {
        this.value = value; // 점수를 설정
    }

    public void increment() {
        value++; // 점수를 1 증가
    }

    // 다른 유용한 메서드나 필드를 추가할 수 있음
}
