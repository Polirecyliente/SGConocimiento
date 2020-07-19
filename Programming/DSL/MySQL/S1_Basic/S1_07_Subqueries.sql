/*
    Subqueries
*/

USE classicmodels;

--T-- subquery example, WHERE field1 IN (SELECT field1 FROM table1), filters the records of field1 to only those from table1
SELECT
    lastName,firstName
FROM
    employees
WHERE
    officecode IN   (SELECT
                        officecode
                    FROM
                        offices
                    WHERE
                        country = 'USA');

--T-- WHERE EXISTS(subquery), filters to the records than are not null in the subquery
SELECT
    customerNumber, customerName
FROM
    customers
WHERE
    EXISTS( SELECT
                1
            FROM
                orders
            WHERE
                orders.customerNumber = customers.customerNumber);