/*
    Sets
*/

USE classicmodels;

--T-- query1 UNION [DISTINCT|ALL] query2, the result is the union of query1 and query2
SELECT
    firstName,
    lastName
FROM
    employees
UNION DISTINCT
SELECT
    contactFirstName,
    contactLastName
FROM
    customers;

--T-- mimic INTERSECT, intersects results with the INNER JOIN
SELECT DISTINCT
    firstName,
    employeeNumber,
    salesRepEmployeeNumber,
    contactFirstName
FROM
    employees
        INNER JOIN
    customers ON employeeNumber = salesRepEmployeeNumber;

--T-- mimic MINUS, gets the difference with the LEFT JOIN, and with the WHERE field1 IS NULL
SELECT
    jobTitle,
    firstName,
    employeeNumber,
    salesRepEmployeeNumber,
    contactFirstName
FROM
    employees
        LEFT JOIN
    customers ON employeeNumber = salesRepEmployeeNumber
WHERE
    salesRepEmployeeNumber IS NULL;