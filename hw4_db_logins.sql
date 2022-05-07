create database hw4_db;

GRANT CREATE, ALTER, DROP, INSERT, UPDATE, SELECT, execute  on hw4_db.* TO 'hw4app'@'%' WITH GRANT OPTION;

use hw4_db;

CREATE TABLE `logins` (
  `uId` int NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT '',
  `password` varchar(60) DEFAULT '',
  `email` varchar(50) DEFAULT '',
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`uId`),
  UNIQUE KEY `UC_login` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
