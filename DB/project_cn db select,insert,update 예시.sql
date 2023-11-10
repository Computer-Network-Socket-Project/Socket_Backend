use project_cn;

-- ex. "2023년 총장배 농구대회"라는 제목의 게임이 시작됨 => 라온 vs 비상, 축구
INSERT INTO GAME_INFO (game_name, sport_type, team_name, game_progress)
VALUES 
	("2023년 총장배 농구대회", 0, "라온", 1),
	("2023년 총장배 농구대회", 0, "비상", 1);

SELECT *
FROM GAME_INFO;

-- ex. "2023년 총장배 농구대회"라는 제목의 게임에서 라온팀이 1점을 득점함
UPDATE GAME_INFO
SET team_score = team_score + 1
WHERE game_name="2023년 총장배 농구대회" and team_name="라온";

SELECT *
FROM GAME_INFO;

-- ex. "2023년 총장배 농구대회"라는 제목의 게임에 좋아요를 누름
UPDATE GAME_INFO
SET great_num = great_num + 1
WHERE game_name="2023년 총장배 농구대회";

SELECT *
FROM GAME_INFO;

-- ex. "2023년 총장배 농구대회"라는 제목의 게임이 종료됨
UPDATE GAME_INFO
SET game_progress = 0
WHERE game_name="2023년 총장배 농구대회";

SELECT *
FROM GAME_INFO;

-- ex. "2023년 총장배 농구대회"라는 제목의 게임에 "라온팀 1점 득점했습니다"라는 채팅이 생김
INSERT INTO CHATTING (GAME_NAME, CHAT)
VALUE ("2023년 총장배 농구대회", "라온팀 1점 득점했습니다");

SELECT *
FROM CHATTING;

-- ex. "2023년 총장배 농구대회"라는 제목의 게임에 "비상팀 000 선수가 부상을 당했습니다."라는 채팅이 생김
INSERT INTO CHATTING (GAME_NAME, CHAT)
VALUE ("2023년 총장배 농구대회", "비상팀 000 선수가 부상을 당했습니다.");

SELECT *
FROM CHATTING;

-- ex. "2023년 총장배 농구대회"라는 제목의 게임에서 "라온팀"에 대한 채팅을 찾고 싶음
SELECT *
FROM CHATTING
WHERE chat like "%라온팀%";
