-- create the databases
CREATE DATABASE IF NOT EXISTS user_database;

-- create the users for each database
CREATE USER 'user_host'@'%' IDENTIFIED BY 'secret';
GRANT CREATE, ALTER, INDEX, LOCK TABLES, REFERENCES, UPDATE, DELETE, DROP, SELECT, INSERT ON `user_host`.* TO 'user_host'@'%';

FLUSH PRIVILEGES;

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');