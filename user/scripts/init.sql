CREATE DATABASE IF NOT EXISTS user_database;

CREATE USER 'user_host'@'%' IDENTIFIED BY 'secret';

GRANT ALL PRIVILEGES ON * . * TO 'user_host'@'%';

FLUSH PRIVILEGES;

