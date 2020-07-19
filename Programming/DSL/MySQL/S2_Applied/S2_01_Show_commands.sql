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

--T-- SHOW FULL TABLES FROM db1
SHOW FULL TABLES FROM testdb;

--T-- DESCRIBE db1.table1
DESCRIBE classicmodels.orders;

--T-- SHOW FULL COLUMNS FROM db1.table1
SHOW FULL COLUMNS FROM classicmodels.employees;