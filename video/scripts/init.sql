-- create the databases
CREATE DATABASE IF NOT EXISTS video_database;

-- create the users for each database
CREATE USER 'video_host'@'%' IDENTIFIED BY 'secret';
GRANT CREATE, ALTER, INDEX, LOCK TABLES, REFERENCES, UPDATE, DELETE, DROP, SELECT, INSERT ON `video_host`.* TO 'video_host'@'%';

FLUSH PRIVILEGES;

--INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
--VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
