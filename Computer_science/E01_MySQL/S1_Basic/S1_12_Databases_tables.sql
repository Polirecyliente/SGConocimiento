/*
    Databases, tables
*/

--T-- USE db1; SELECT DATABASE(), the DATABASE() function returns the current database
USE classicmodels;
SELECT DATABASE();

--T-- CREATE DATABASE [IF NOT EXISTS] db1
CREATE DATABASE IF NOT EXISTS deldb1;

--T-- CREATE DATABASE db1 CHARACTER SET ascii COLLATE ascii_general_ci, the collation defines the order of the characters to make it an ordered set
CREATE DATABASE IF NOT EXISTS deldb1 CHARACTER SET ascii COLLATE ascii_general_ci;

--T-- SHOW DATABASES
SHOW DATABASES;

--T-- DROP DATABASE [IF EXISTS] db1
DROP DATABASE IF EXISTS deldb1;

--T-- CREATE TABLE [IF NOT EXISTS] tableName (fieldNames) [ENGINE=value]
CREATE TABLE IF NOT EXISTS db1.t3
(
    idFld1 INT AUTO_INCREMENT,
    idFld2 INT,
    fld1 VARCHAR(15) NOT NULL DEFAULT "NoVal",
    dateFld DATE,
    numFld TINYINT,
    descrFld TEXT,
    PRIMARY KEY (idFld1,idFld2)
) ENGINE=INNODB;

--T-- CREATE TABLE table1 LIKE table2
CREATE TABLE IF NOT EXISTS t3 LIKE t2;

--T-- CREATE TABLE child_table1 (fields, fk_field [INT], FOREIGN KEY (fk_field) REFERENCES parent_table1 (parent_table1.key_field) ON DELETE CASCADE)
CREATE TABLE buildings
(
    building_no INT PRIMARY KEY AUTO_INCREMENT,
    building_name VARCHAR(255) NOT NULL,
    building_address VARCHAR(255) NOT NULL
);
CREATE TABLE rooms
(
    room_no INT PRIMARY KEY AUTO_INCREMENT,
    room_name VARCHAR(255) NOT NULL,
    building_noFK INT NOT NULL,
    FOREIGN KEY (building_noFK)
        REFERENCES buildings (building_no)
        ON DELETE CASCADE
);
DELETE FROM buildings
WHERE building_no = 2;

--T-- [CREATE|DROP] TEMPORARY TABLE query1
CREATE TEMPORARY TABLE tmpTbl
SELECT
    customerNumber,
    customerName
FROM
    customers
LIMIT 10;
SELECT * FROM tmpTbl;
DROP TEMPORARY TABLE tmpTbl;

--T-- ALTER TABLE table1 CHANGE COLUMN field1 field1_new DECIMAL(11), this renames field1 to field1_new and changes its data type
ALTER TABLE t3
CHANGE COLUMN idFld2 idFld2mv DECIMAL(11);

--T-- ALTER TABLE table1 ADD COLUMN new_field data_type [FIRST|AFTER field1]
ALTER TABLE t3
ADD COLUMN newFld DECIMAL(3,2) AFTER fld1;

--T-- ALTER TABLE table1 DROP COLUMN field1
ALTER TABLE t3
DROP COLUMN newFld;

--T-- ALTER TABLE table1 RENAME TO table1_new
ALTER TABLE t3
RENAME TO t3new;

--T-- RENAME TABLE table1 TO table1_new
RENAME TABLE t3new TO t3,
             t2 TO t2new;

--T-- DROP TABLE [IF EXISTS] tbl1
DROP TABLE IF EXISTS t3new;

--T-- TRUNCATE TABLE table1, this deletes all data in the table but leaves the headers
TRUNCATE TABLE t3;