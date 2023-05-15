-- create the databases
CREATE DATABASE IF NOT EXISTS recommendation_database;

CREATE USER 'recommendation_host'@'%' IDENTIFIED BY 'secret';

GRANT ALL PRIVILEGES ON * . * TO 'recommendation_host'@'%';

FLUSH PRIVILEGES;

use recommendation_database;

CREATE TABLE useraction (
    user_action_id INT PRIMARY KEY,
    user_id INT,
    video_id INT,
    action VARCHAR(255)
); 

