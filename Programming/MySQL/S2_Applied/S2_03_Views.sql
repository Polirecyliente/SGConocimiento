/*
    Views
*/

USE classicmodels;

--T-- CREATE VIEW view1 AS query1
CREATE VIEW view1 AS
    SELECT * FROM orders INNER JOIN orderdetails USING(orderNumber);