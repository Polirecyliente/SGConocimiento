/*
    Filters
*/

USE classicmodels;

--T-- WHERE (field1 <> 'value1') OR (field2 > 30 AND field3 < 67) OR (field4 = "Keyword")
SELECT
    lastName,
    firstName,
    jobTitle
FROM
    employees
WHERE
    jobTitle <> 'Sales Rep';

--T-- WHERE field1 = 'value1' AND field2 = 'value2'
SELECT
    customerName,
    country,
    state,
    creditlimit
FROM
    customers
WHERE country = 'USA'
 AND state = 'CA'
 AND creditlimit > 100000;

--T-- OR (same logic as with AND)
SELECT
    customerName,
    country,
    creditlimit
FROM
    customers
WHERE(country = 'USA'
 OR country = 'France')
 AND creditlimit > 100000;

--T-- WHERE field [NOT] IN ('value1','value2')
SELECT
    officeCode,
    city,
    phone,
    country
FROM
    offices
WHERE
    country NOT IN ('USA', 'France');

--T-- WHERE field BETWEEN 'value1' AND 'value2'
SELECT
    productCode,
    productName,
    buyPrice
FROM
    products
WHERE
    buyPrice BETWEEN 20 AND 100;

--T-- The falues for the BETWEEN clause can be strings too, in that case, the collation order is used

SELECT * FROM db1.table1;

+--------+--------+--------+
| field1 | field2 | field3 |
+--------+--------+--------+
|     12 | bcde   |     54 |
|     17 | mno    |    107 |
|     28 | vwxyz  |    500 |
+--------+--------+--------+

SELECT * FROM db1.table1 WHERE field2 BETWEEN 'ghi' AND 'qrst';

+--------+--------+--------+
| field1 | field2 | field3 |
+--------+--------+--------+
|     17 | mno    |    107 |
+--------+--------+--------+


--T-- WHERE field LIKE '%ending'; the percent % acts as a regex quantifier
SELECT
    employeeNumber,
    lastName,
    firstName
FROM
    employees
WHERE
    lastName LIKE '%on';

--T-- LIMIT offsetN, countN, this limits the returned records to countN starting at offsetN
SELECT
    productName,
    buyPrice
FROM
    products
ORDER BY
    buyPrice DESC
LIMIT 1, 1;

--T-- WHERE field IS NULL, this returns the records where field has a null value
SELECT
    customerName,
    country,
    salesrepemployeenumber
FROM
    customers
WHERE
    salesrepemployeenumber IS NULL
ORDER BY customerName;