/*
    Grouping
*/

USE classicmodels;

--T-- GROUP BY field [DESC|ASC]
SELECT
    status, COUNT(*)
FROM
    orders
GROUP BY status;

--T-- SELECT SUM(field1 * field2) ... HAVING field3 > value1
SELECT
    orderNumber,
    SUM(quantityOrdered) AS itemsCount,
    SUM(priceEach*quantityOrdered) AS total
FROM
    orderdetails
GROUP BY orderNumber
HAVING total > 1000 AND itemsCount > 600;

--T-- IF(condition, true case, false case) ... GROUP BY field1 WITH ROLLUP, creates a subtotal per value of field1 ... GROUPING(field1), returns 1 if row is NULL because of rollup of field1 values
SELECT
    IF(GROUPING(orderYear),
        'All Years',
        orderYear) ordersYear,
    IF(GROUPING(productLine),
        'All Product Line',
        productLine) productsLine,
    SUM(orderValue) totalOrderValue
FROM
    sales
GROUP BY
    orderYear,
    productLine
WITH ROLLUP;