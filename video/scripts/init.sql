-- create the databases
CREATE DATABASE IF NOT EXISTS video_database;

CREATE USER 'video_host'@'%' IDENTIFIED BY 'secret';

GRANT ALL PRIVILEGES ON * . * TO 'video_host'@'%';

FLUSH PRIVILEGES;

use video_database;

CREATE TABLE category (
    category_id INT PRIMARY KEY,
    category VARCHAR(255)
); 

CREATE TABLE video (
    video_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    title VARCHAR(50),
    resume VARCHAR(255),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
); 


INSERT INTO category (category_id, category)
VALUES (0, 'Sports');

INSERT INTO category (category_id, category)
VALUES (1, 'Outdoor');


INSERT INTO category (category_id, category)
VALUES (2, 'Music');


INSERT INTO category (category_id, category)
VALUES (3, 'Gaming');


INSERT INTO category (category_id, category)
VALUES (4, 'DIY');


INSERT INTO category (category_id, category)
VALUES (5, 'Food');


INSERT INTO category (category_id, category)
VALUES (6, 'Programming');


INSERT INTO category (category_id, category)
VALUES (7, 'Animals');


INSERT INTO category (category_id, category)
VALUES (8, 'Education');

INSERT INTO video (title, user_id, resume, category_id)
VALUES ('Food video', '10', 'amagermanden er på fri fod', 7);

INSERT INTO video (title, user_id, resume, category_id)
VALUES ('animal video', '10', 'amagermanden er på fri hoved', 7);

INSERT INTO video (title, user_id, resume, category_id)
VALUES ('random video', '10', 'amagermanden er på fri arm', 6);

INSERT INTO video (title, user_id, resume, category_id)
VALUES ('test video', '11', 'amagermanden er på fri ben', 6);

INSERT INTO video (title, user_id, resume, category_id)
VALUES ('lol video', '11', 'amagermanden er på fri hånd', 6);

INSERT INTO video (title, user_id, resume, category_id)
VALUES ('programming video', '11', 'amagermanden er på fri mave', 7);
