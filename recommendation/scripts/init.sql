-- create the databases
CREATE DATABASE IF NOT EXISTS recommendation_database;

CREATE USER 'recommendation_host'@'%' IDENTIFIED BY 'secret';

GRANT ALL PRIVILEGES ON * . * TO 'recommendation_host'@'%';

FLUSH PRIVILEGES;

use recommendation_database;

CREATE TABLE UserAction (
    user_action_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    video_id INT,
    category_id INT,
    action VARCHAR(255)
); 

INSERT INTO UserAction (user_id, video_id, category_id, action)
VALUES (10, 1, 5, 'watch-event');

INSERT INTO UserAction (user_id, video_id, category_id, action)
VALUES (10, 1, 5, 'rate-event');


