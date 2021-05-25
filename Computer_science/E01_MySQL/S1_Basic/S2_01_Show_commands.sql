/*
    Show commands
*/

--T-- SHOW PROCEDURE STATUS
SHOW PROCEDURE STATUS;

--T-- SHOW PROCESSLIST
SHOW PROCESSLIST;

--T-- list all MySQL users and their valid host with
SELECT user,host FROM mysql.user;

--T-- SHOW GLOBAL STATUS to see global variables
SHOW GLOBAL STATUS;

--T-- SHOW DATABASES|SCHEMAS
SHOW SCHEMAS;

--T-- Show the tables from a database.
SHOW TABLES FROM database1;

--T-- SHOW FULL TABLES FROM db1
SHOW FULL TABLES FROM testdb;

--T-- DESCRIBE db1.table1
DESCRIBE classicmodels.orders;

--T-- Show the columns from a table
SHOW COLUMNS FROM db1.table1;

--T-- SHOW FULL COLUMNS FROM db1.table1
SHOW FULL COLUMNS FROM classicmodels.employees;