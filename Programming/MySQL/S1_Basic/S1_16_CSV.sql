/*
    CSV
*/

--T-- CSV stands for Comma Separated Values
--T-- CSV import and export

USE classicmodels;
--T-- query1 INTO OUTFILE '/path/to/output_file.csv' FIELDS ENCLOSED BY '' TERMINATED BY '' ESCAPED BY '' LINES TERMINATED BY ''
SELECT
    orderNumber,orderDate,comments
FROM
    orders
WHERE
    comments IS NULL
INTO OUTFILE '/home/jul/serverPolirecyl/mysql-files/S1_15_Aux01.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ';'
ESCAPED BY '\\'
LINES TERMINATED BY '\r\n';

CREATE TABLE t3(fld1 CHAR(5),fld2 CHAR(10),fld3 CHAR(3));
--T-- LOAD DATA INFILE '/path/to/input_file.csv' INTO TABLE table1 IGNORE number1 ROWS
LOAD DATA INFILE '/home/jul/serverPolirecyl/mysql-files/S1_15_Aux01.csv'
INTO TABLE t3
FIELDS ENCLOSED BY '"'
TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 5 ROWS;
SELECT * FROM t3;