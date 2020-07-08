/*
    Modifying data
*/

USE testdb;

--T-- INSERT INTO table1(field1,field2,field3) VALUES ('val1field1','val1field2','val1field3'), ('val2field1','val2field2','val2field3')
INSERT INTO
    sales(product_id,store_id,quantity,sales_date)
VALUES
    (3,2,5,'2017-02-26'),
    (3,2,DEFAULT,CURRENT_DATE()),
    (1,1,7,'2018-05-24');

--T-- INSERT INTO table(fields) query1, where query1 has values originated from a result set
INSERT INTO
    sales(product_id,store_id,quantity,sales_date)
SELECT
    p.id,1,21,'2013-06-07'
FROM
    products p;

--T-- INSERT IGNORE INTO table(fields), inserts values into the table ignoring errors that arise
INSERT IGNORE INTO
    sales(product_id,quantity)
VALUES
    (1,12),
    ("b",9),
    (2,9);

--T-- REPLACE INTO table1(field1,field2) VALUES (value1,'value2')
REPLACE INTO sales(product_id,store_id,quantity,sales_date)
VALUES (2,NULL,14,'2015-05-25');

--T-- REPLACE INTO table1 SET field1 = value1, field2 = 'value2'
REPLACE INTO salesWinFun
SET sale = 250,
    fiscal_year = 2018,
    sales_employee = "Alice";

USE classicmodels;

--T-- UPDATE [IGNORE] table1 SET field1 = 'value1' WHERE condition
UPDATE IGNORE
    employees
SET
    lastName = 'Hill',
    email = 'mary.hill@classicmodelcars.com'
WHERE employeeNumber = 1056;

--T-- DELETE FROM table1 WHERE condition
DELETE FROM employees
WHERE officeCode = 8
ORDER BY officeCode
LIMIT 5;

--T-- PREPARE statement1 FROM 'query1'
--T-- SET @queriedVal = 'value1'
--T-- EXECUTE statement1 USING @queriedVal
--T-- DEALLOCATE PREPARE statement1
PREPARE statement1 FROM
'SELECT
    productCode, productName
FROM
    products
WHERE
    productCode = ?';
SET @prodCode1 = 'S10_1678';
EXECUTE statement1 USING @prodCode1;
DEALLOCATE PREPARE statement1;