-- show databases;

create database if not exists project_cn;

use project_cn;

-- show tables;

DROP TABLE if exists ADMIN_INFO, GAME_INFO, CHATTING;

CREATE TABLE ADMIN_INFO (
    admin_id varchar(20) NOT NULL,
    admin_ps int NOT NULL
);


CREATE TABLE GAME_INFO (
	id			int auto_increment	primary key,
	game_name	varchar(20)	NOT NULL unique,
	team1_name	varchar(6)	NOT NULL,
	team1_score	int	NOT NULL default 0,
	team2_name	varchar(6)	NOT NULL,
	team3_score	int	NOT NULL default 0,
	great_num	int	NOT NULL	DEFAULT 0,
    sport_type	boolean	NOT NULL	DEFAULT 0,
    game_datetime	datetime	NOT NULL	DEFAULT NOW(),
    game_half		boolean	NOT NULL	DEFAULT 0,
    game_progress	boolean	NOT NULL	DEFAULT 0
);

CREATE TABLE CHATTING (
	-- idx	int	NOT NULL,
	game_name	varchar(20)	NOT NULL,
	chat	VARCHAR(50)	NULL,
	chat_datetime	datetime	NOT NULL	DEFAULT NOW()
);

ALTER TABLE ADMIN_INFO ADD CONSTRAINT PK_ADMIN PRIMARY KEY (
	admin_id
);

-- ALTER TABLE GAME_INFO ADD CONSTRAINT PK_GAME_INFO PRIMARY KEY (
-- 	game_name,
--     team_name
-- );

-- ALTER TABLE CHATTING ADD CONSTRAINT PK_CHATTTING PRIMARY KEY (
-- 	idx,
-- 	game_name
-- );

ALTER TABLE CHATTING ADD CONSTRAINT FK_GAME_INFO_TO_CHATTTING_1 FOREIGN KEY (
	game_name
)REFERENCES GAME_INFO (
	game_name
);
