/*
    Constraints
*/

USE classicmodels;
DROP TABLE IF EXISTS t3;

--T-- in the table creation, field1 data_type NOT NULL, constraints the records in field1 to be not null
CREATE TABLE t3(fld1 INT NOT NULL);
DESCRIBE t3;

--T-- PRIMARY KEY(key_field), constraints key_field to be unique and the primary key of the table
CREATE TABLE t3(idFld1 INT,idFld2 INT,
                        PRIMARY KEY(idFld1,idFld2));
DESCRIBE t3;

--T-- primary key with ALTER TABLE
DROP TABLE IF EXISTS t3;
CREATE TABLE t3(alterid INT, idxFld INT);
ALTER TABLE t3 ADD PRIMARY KEY(alterid);

--T-- UNIQUE INDEX index_field, the index_field is constrained to be unique
ALTER TABLE t3 ADD UNIQUE INDEX idx1 (idxFld ASC);
DESCRIBE t3;

--T-- [CONSTRAINT constraint_name] FOREIGN KEY [fk_name] (fk_field) REFERENCES parent_table (parent_table.key_field) [ON DELETE reference_option1 ON UPDATE reference_option2], without constraint_name or fk_name, names are given automatically
--T-- the reference_option can be any of CASCADE (changes in parent, cascade to child), SET NULL (changes in parent, set null in child), RESTRICT (changes in parent are rejected if child has a matching row with parent), NO ACTION (same as RESTRICT)
CREATE TABLE t3(alterfk INT, fid1 VARCHAR(50),
            CONSTRAINT ctrai1 FOREIGN KEY fk_name1 (fid1)
            REFERENCES t2(id) ON UPDATE CASCADE ON DELETE RESTRICT);
DESCRIBE t3;

--T-- foreign key with ALTER TABLE
ALTER TABLE t3 ADD CONSTRAINT ctrai2 FOREIGN KEY fk_name2 (alterfk)
            REFERENCES t1(id) ON UPDATE CASCADE ON DELETE CASCADE;
DESCRIBE t3;

--T-- DROP FOREIGN KEY constraint_name
ALTER TABLE t3 DROP FOREIGN KEY ctrai1;
DESCRIBE t3;

--T-- UNIQUE constraint, makes values unique in the field
CREATE TABLE t3 (fld1 INT UNIQUE, fld2 INT, fld3 INT, 
        CONSTRAINT ctrai3 UNIQUE(fld2,fld3));

--T-- SHOW INDEX, SHOW CREATE TABLE
SHOW INDEX FROM t3;
SHOW CREATE TABLE t3;}

--T-- DROP INDEX
DROP INDEX ctrai3 ON t3;
ALTER TABLE t3 DROP INDEX fld1;