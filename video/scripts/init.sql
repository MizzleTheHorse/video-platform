-- create the databases
CREATE DATABASE IF NOT EXISTS video_database;

CREATE USER 'video_host'@'%' IDENTIFIED BY 'secret';

GRANT ALL PRIVILEGES ON * . * TO 'video_host'@'%';

FLUSH PRIVILEGES;

use video_database;

CREATE TABLE category (
    category_id INT PRIMARY KEY,
    category VARCHAR(255),
    description VARCHAR(255)
); 

CREATE TABLE video (
    video_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    title VARCHAR(50),
    resume VARCHAR(255),
    category VARCHAR(255),
    category_id INT,
    video_rating INT,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
); 


INSERT INTO category (category_id, category, description)
VALUES (9, 'Sports', 'The sports category features all the themes and disciplines regarding sports. ');

INSERT INTO category (category_id, category, description)
VALUES (1, 'Outdoor', 'for everything outdoors');


INSERT INTO category (category_id, category, description)
VALUES (2, 'Music', 'unleash the creativity to produce new art from sounds');


INSERT INTO category (category_id, category, description)
VALUES (3, 'Gaming', 'l33t gaymer');


INSERT INTO category (category_id, category, description)
VALUES (4, 'DIY', 'DO it your fucking self');


INSERT INTO category (category_id, category, description)
VALUES (5, 'Food', 'mmmmm this category is yummy');


INSERT INTO category (category_id, category, description)
VALUES (6, 'Programming','Nerds everywhere');


INSERT INTO category (category_id, category, description)
VALUES (7, 'Animals',' they are so fucking cute');

INSERT INTO category (category_id, category, description)
VALUES (8, 'Education', 'Time to get smart and learn some new stuff');

INSERT INTO video (title, user_id, resume, category , category_id)
VALUES ('Pasta tutorial 101', '10', 'How to make Pasta for complete dummies and software engineers', 'Food', 5);

INSERT INTO video (title, user_id, resume, category, category_id)
VALUES ('Cat slapping another cat', '10', 'These silly animals will just slap each other all day', 'Animals', 7);

INSERT INTO video (title, user_id, resume, category, category_id)
VALUES ('Python Tutorial part 1', '10', 'In this episode of the programming dude, we are going to look at python, a great langauage everyone can learn!', 'Programming', 6);

INSERT INTO video (title, user_id, resume, category,  category_id)
VALUES ('Javascript death tutorial', '11', 'You cant learn javascript without actively hating yourself and eveyone around you, join the club', 'Programming', 6);

INSERT INTO video (title, user_id, resume, category, category_id)
VALUES ('assembly tutorial for experts, part 420', '11', 'Why are we even here, just to suffer?', 'Programming', 6);

INSERT INTO video (title, user_id, resume, category, category_id)
VALUES ('Big python escapes Zoo, must watch!', '11', 'Snek go brrrrrr.','Animals', 7);

INSERT INTO video (title, user_id, resume, category, category_id)
VALUES ('Hiking in Nepal mountains', '10', 'This video is about hiking in the nepalese mountains, with a beautfil scenary!','Outdoor', 1);