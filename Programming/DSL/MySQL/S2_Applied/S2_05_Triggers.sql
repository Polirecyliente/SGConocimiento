/*
    Triggers
*/

USE classicmodels;

--T-- DROP TRIGGER trigger1
--T-- CREATE TRIGGER trigger1 (BEFORE|AFTER) (INSERT ON|UPDATE ON|DELETE ON) table1 FOR EACH ROW BEGIN data_modify END
DROP TRIGGER before_t3_update;
CREATE TRIGGER before_t3_update
    BEFORE UPDATE ON t3
    FOR EACH ROW
BEGIN
    INSERT INTO sales(productLine,orderValue) VALUES("trigg",1.1);
END;

USE classicmodels;
UPDATE t3 SET fld1 = "updat" WHERE fld1 = "10106";
SELECT * FROM sales;