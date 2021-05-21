/*
    Join
*/

USE classicmodels;

--T-- SELECT CONCAT_WS('-', field1 , field2 ) AS `str1` ... ORDER BY `str1` ... in CONCAT_WS WS stands for With Separator. AS serves to create aliases
SELECT
    CONCAT_WS(', ', lastName, firstName) AS `Full name`
FROM
    employees
ORDER BY
    `Full name`;

--T-- FROM table1 t1 INNER JOIN table2 t2 ON t1.field = t2.field
SELECT
    orderNumber,
    productName,
    msrp,
    priceEach
FROM
    products p
        INNER JOIN
    orderdetails o ON p.productcode = o.productcode
        AND p.msrp > o.priceEach
WHERE
    p.productcode = 'S10_1678';

--T-- FROM table1 t1 LEFT JOIN table2 t2 USING (field1), having field1 belonging to both tables
SELECT
    c.customerNumber,
    customerName,
    orderNumber,
    status
FROM
    customers c
LEFT JOIN orders USING (customerNumber);

--T-- SELECT CONCAT(field1,' ',field2) concatenates field1 and field2 with a space between ... FROM table1 t1 RIGHT JOIN table t2 ON t1.field3 = t2.field4 
SELECT
    CONCAT(e.firstName,' ', e.lastName) salesman,
    e.jobTitle,
    customerName
FROM
    employees e
        RIGHT JOIN
    customers c ON e.employeeNumber = c.salesRepEmployeeNumber
ORDER BY customerName;

--T-- FROM table1 CROSS JOIN table2
USE testdb;
SELECT
    store_name, product_name
FROM
    stores
        CROSS JOIN
    products;