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
    action VARCHAR(255)
); 

INSERT INTO UserAction (user_id, video_id, action)
VALUES (10, 1, 'watch-event');

INSERT INTO UserAction (user_id, video_id, action)
VALUES (10, 1, 'watch-event');

INSERT INTO UserAction (user_id, video_id, action)
VALUES (10, 2, 'watch-event');

INSERT INTO UserAction (user_id, video_id, action)
VALUES (10, 3, 'rate-event');

INSERT INTO UserAction (user_id, video_id, action)
VALUES (10, 1, 'rate-event');

INSERT INTO UserAction (user_id, video_id, action)
VALUES (10, 1, 'rate-event');

INSERT INTO UserAction (user_id, video_id, action)
VALUES (10, 1, 'rate-event');

