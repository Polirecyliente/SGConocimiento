/*
    Sorting
*/

USE classicmodels;

--T-- ORDER BY field1 DESC, field2 ASC
SELECT
    contactLastName,
    contactFirstName
FROM
    customers
ORDER BY 
    contactLastName DESC,
    contactFirstName ASC;

--T-- ORDER BY FIELD(field, 'value1', 'value2')
SELECT
    orderNumber, status
FROM
    orders
ORDER BY FIELD(status,
        'In Process',
        'On Hold',
        'Cancelled',
        'Resolved',
        'Disputed',
        'Shipped');