/*
    Stored procedures
*/

USE classicmodels;
--T-- DROP PROCEDURE procedure1
--T-- CREATE PROCEDURE procedure1 (IN input_var1 data_type1, OUT output_var1 data_type2) BEGIN DECLARE local_var1; SET lhs = rhs; query1; END, where DECLARE serves to declare variables, SET is to set relations between lhs and rhs expressions
--T-- CALL procedure1(input_value,output_var)
DROP PROCEDURE procedureName;
CREATE PROCEDURE procedureName(IN param1 DOUBLE, OUT param2 INT)
    BEGIN
        DECLARE var1 INT(10) DEFAULT 2;
        SET param2 = var1;
        SELECT buyPrice FROM products WHERE buyPrice < param1;
    END;

CALL procedureName(23.1,@extVar1);
SELECT @extVar1;