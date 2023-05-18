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
VALUES ('Food video', '10', 'Video omkring mad', 'Food', 5);

INSERT INTO video (title, user_id, resume, category, category_id)
VALUES ('animal video', '10', 'Cute fucking doggos', 'Animals', 7);

INSERT INTO video (title, user_id, resume, category, category_id)
VALUES ('random video', '10', 'amagermanden er stadig sluppet fri', 'Programming', 6);

INSERT INTO video (title, user_id, resume, category,  category_id)
VALUES ('test video', '11', 'amagermanden er fanget igen', 'Programming', 6);

INSERT INTO video (title, user_id, resume, category, category_id)
VALUES ('lol video', '11', 'amagermanden er ked af det', 'Programming', 6);

INSERT INTO video (title, user_id, resume, category, category_id)
VALUES ('programming video', '11', 'JEG kan godt lide pythons','Animals', 7);
