/*
    CTE
*/

--T-- CTE stands for Common Table Expressions, they are named temporary result sets

USE classicmodels;

--T-- WITH named_result_cte (field1, field2) AS (query) SELECT field1 FROM named_result_cte, this queries in named_result_cte which is a temporary table
WITH customers_in_usa AS (
    SELECT
        customerName, state
    FROM
        customers
    WHERE
        country = 'USA'
) SELECT
    customerName
FROM
    customers_in_usa
WHERE
    state = 'CA'
ORDER BY customerName;

--T-- WITH RECURSIVE named_cte AS (query UNION ALL recursive_query) SELECT field1 FROM named_cte, the recursive_query must include the named_cte table
WITH RECURSIVE employee_paths
AS (
    SELECT
        employeeNumber,
        reportsTo managerNumber,
        officeCode,
        1 lvl
    FROM
        employees
    WHERE
        reportsTo IS NULL
    UNION ALL
    SELECT
        e.employeeNumber,
        e.reportsTo,
        e.officeCode,
        lvl+1
    FROM
        employees e
            INNER JOIN
        employee_paths ep ON ep.employeeNumber = e.reportsTo
    )
SELECT
    employeeNumber,
    managerNumber,
    lvl,
    city
FROM
    employee_paths ep
        INNER JOIN
    offices o USING (officeCode)
ORDER BY lvl,city;