/*
    Transactions
*/

USE classicmodels;

--T-- START TRANSACTION; DELETE FROM table1; COMMIT; the delete statement can be any other modification like an insert, update, replace
START TRANSACTION;
SELECT
    @nextOrder:=MAX(orderNumber) + 1
FROM
    orders;
INSERT INTO 
    orders(orderNumber,orderDate,requiredDate,
    shippedDate,status,customerNumber)
VALUES (@nextOrder,'2020-02-20','2020-03-20',
    '2020-03-21','In Process',145);
INSERT INTO
    orderdetails(orderNumber,productCode,quantityOrdered,
    priceEach,orderLineNumber)
VALUES  (@nextOrder,'S18_1749',30,
        '136',1),
        (@nextOrder,'S18_2248',50,
        '55.09',2);
COMMIT;

--T-- START TRANSACTION; DELETE FROM table1; ROLLBACK; the delete statement can be any other modification like an insert, update, replace
START TRANSACTION;
DELETE FROM orderdetails;
ROLLBACK;

--T-- LOCK TABLES table1 READ|WRITE; INSERT INTO table1(idField,field1) VALUES (5,"value1"); UNLOCK TABLES;
LOCK TABLES t1 READ;
INSERT INTO
    t1(id,pattern)
VALUES
    (5,"patt5");
UNLOCK TABLES;