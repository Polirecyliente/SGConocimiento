/*
    Data types
*/

USE classicmodels;
DROP TABLE IF EXISTS t3;
CREATE TABLE IF NOT EXISTS t3
(
--T-- Numeric data types
    fld1 TINYINT(5) UNSIGNED ZEROFILL DEFAULT 255,
    fld2 SMALLINT(5) DEFAULT 32767,
    fld3 MEDIUMINT(5) DEFAULT 8388607,
    fld4 INT(10) ZEROFILL DEFAULT 2147483647,
    fld4a INTEGER,
    fld5 BIGINT DEFAULT 9223372036854775807,
    fld6 DECIMAL(65,30) UNSIGNED ZEROFILL DEFAULT 1.3,
    fld6a DEC(5,2),
    fld6b FIXED(5,2),
    fld6c NUMERIC(5,2),
    fld7 FLOAT DEFAULT 1.4,
    fld8 DOUBLE DEFAULT 1.5,
    fld9 BIT(64) DEFAULT b'1101001',
    fld10 BOOLEAN DEFAULT FALSE,

--T-- String data types
    fld11 CHAR(255) DEFAULT "NoValChar",
    fld12 VARCHAR(60000) DEFAULT "NoValVarCh",
    fld13 BINARY(9) DEFAULT "NoValBin",
    fld14 VARBINARY(100) DEFAULT "NoValVarbin",
    fld15 TINYBLOB,
    fld16 BLOB,
    fld17 MEDIUMBLOB,
    fld18 LONGBLOB,
    fld19 TINYTEXT,
    fld20 TEXT,
    fld21 MEDIUMTEXT,
    fld22 LONGTEXT,

--T-- Date and time data types
    fld25 DATE,
    fld26 TIME(6),
    fld27 DATETIME(6),
    fld28 TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    fld29 YEAR(4),

--T-- JSON, ENUM, and SET data types
    fld30 JSON,
    fld23 ENUM ('opt1','opt2','opt3'),
    fld24 SET ('elOne','elTwo','elThree')
);

DESCRIBE t3;
INSERT INTO
    t3(fld30,fld23,fld24)
VALUES
    ('{"prop1":"value1","prop2":5}','opt2','elTwo');
SELECT
    fld30->'$.prop1', fld23, fld24
FROM
    t3;