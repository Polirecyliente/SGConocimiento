/*
    Builtin functions
*/

USE classicmodels;

--T-- aggregate, string, and control flow functions

--T-- COUNT(*), in the following example COUNT(*) counts the amount of products per product line, because of the GROUP BY clause
SELECT
    productLine,
    COUNT(*)
FROM
    products
GROUP BY productLine;

--T-- SUM(field1), calculates the sum of the field1 values
SELECT
    SUM(quantityOrdered*priceEach) total
FROM
    orderdetails
WHERE
    orderNumber = 10100;

--T-- CONCAT(field1,'str1',field2), concatenates field1 and field2 using str1 in between
SELECT
    CONCAT(contactFirstName, ' ', contactLastName) Fullname
FROM
    customers;

--T-- CONCAT_WS('str1',field1,field2,field3), concatenates field1, field2, and field3 using str1 as a separator
SELECT CONCAT_WS('\n',
            CONCAT_WS(' ',contactLastName,contactFirstName),
            addressLine1,
            CONCAT_WS(' ',postalCode,city),
            country,
            '\n') AS Customer_Address
FROM
    customers;

--T-- IF(condition, true case, false case)
SELECT
    customerNumber,
    customerName,
    IF(state IS NULL, 'N/A', state) stateOfOrigin,
    country
FROM
    customers;

--T-- date and time, comparison, and math functions

--T-- YEAR('year-mt-dy')
SELECT YEAR('2014-06-23');

--T-- NOW() returns the time at execution, CURRENT_DATE() returns the current date, CURRENT_TIME() returns the current time, UTC_TIME() returns the Universal Time Coordinate time
SELECT NOW();
SELECT CURRENT_DATE();
SELECT CURRENT_TIME();
SELECT UTC_TIME();

--T-- window functions

--T-- window functions operate over a window that surrounds the current row in the execution

USE testdb;

--T-- FUN1(field1) OVER(PARTITION BY partition_field ORDER BY order_field), the FUN1() OVER () causes FUN1() to be a window function. The default frame of the window extends from the beginning of the partition up to the current row. Each partition starts at each value in partition_field, and each partition is ordered according to the order_field
SELECT
    fiscal_year,
    sales_employee,
    sale,
    SUM(sale) OVER (PARTITION BY fiscal_year ORDER BY sale) total_sales
FROM
    salesWinFun;

USE classicmodels;

--T-- ROW_NUMBER() OVER ()
SELECT
    ROW_NUMBER() OVER (
    PARTITION BY productLine
    ORDER BY productName
    ) row_num,
        productName,
        productLine
FROM
    products;

--T-- other functions

--T-- CAST('date_string' AS DATETIME), casts date_string as data type DATETIME
SELECT
    orderNumber,
    requiredDate
FROM
    orders
WHERE requiredDate BETWEEN CAST('2003-01-01' AS DATETIME)
                        AND CAST('2003-01-31' AS DATETIME);