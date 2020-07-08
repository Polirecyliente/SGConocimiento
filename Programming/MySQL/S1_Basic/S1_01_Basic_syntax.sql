/*
    Basic syntax
*/

--T-- install and work with MySQL in VS Code
-- $ sudo apt install mysql-server
--T-- on VS Code install the MySQL extension

--T-- command blocks for querying data, SELECT, FROM, SELECT DISTINCT

USE classicmodels;

--T-- SELECT field FROM table
SELECT 
    lastname, firstname, jobtitle 
FROM 
    employees;

--T-- the asterisk operator * selects all records
SELECT * FROM employees;

--T-- SELECT DISTINCT field1, field2 FROM table WHERE condition
SELECT DISTINCT
    state, city
FROM
    customers
WHERE
    state IS NOT NULL
ORDER BY state, city;

--T-- COUNT(DISTINCT field1) ... WHERE field2 = 'value'
SELECT
    COUNT(DISTINCT state)
FROM
    customers
WHERE
    country = 'USA';