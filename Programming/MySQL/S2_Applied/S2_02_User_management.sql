/*
    User management
*/

--T-- CREATE USER [IF NOT EXISTS] user1@host1 IDENTIFIED BY 'password_string'
CREATE USER IF NOT EXISTS delUser@localhost IDENTIFIED BY 'delUserP4$$';
CREATE USER IF NOT EXISTS testUser@localhost IDENTIFIED BY 'tUserP4$$';

--T-- GRANT privilege1 ON db1.table1 TO user1@host1, where privilege1 can be a subset of ALL PRIVILEGES, INSERT, SELECT, UPDATE, DELETE
GRANT INSERT, SELECT, UPDATE, DELETE ON testdb.sales 
TO delUser@localhost;

--T-- GRANT privilege1(field1),privilege2(field2) ON db1.table1 TO user1@host1
GRANT SELECT(field2T) ON testdb.table1T TO delUser@localhost;

--T-- GRANT EXECUTE ON PROCEDURE procedure1 TO user1@host1
GRANT EXECUTE ON PROCEDURE classicmodels.procedureName TO delUser@localhost;

--T-- GRANT PROXY ON user_proxied TO user1@host1, here user1 gets all the privileges from user_proxied
GRANT PROXY ON testUser TO delUser@localhost;

--T-- REVOKE privilege1(field1) ON db1.table1|user_proxied FROM user1, here privilege1 can also take the value PROXY without field1
REVOKE PROXY ON testUser FROM delUser@localhost;
REVOKE SELECT(field2T) ON testdb.table1T FROM delUser@localhost;
REVOKE UPDATE ON testdb.sales FROM delUser@localhost;

--T-- CREATE ROLE role1@host1
CREATE ROLE midPriviRole1@localhost, role2@localhost;
GRANT SELECT(field1T) ON testdb.table1T TO midPriviRole1@localhost;
GRANT midPriviRole1@localhost TO delUser@localhost;

--T-- SET DEFAULT ROLE role1@host1 TO user1@host1
SET DEFAULT ROLE midPriviRole1@localhost TO delUser@localhost;

--T-- SHOW GRANTS FOR user1@host1 USING role1@host1
SHOW GRANTS FOR delUser@localhost USING midPriviRole1@localhost;
SHOW GRANTS FOR midPriviRole1@localhost;

--T-- SET PASSWORD FOR user1@host1 = 'password_string'
SET PASSWORD FOR delUser@localhost = 'PassNum3';

--T-- FLUSH PRIVILEGES
FLUSH PRIVILEGES;

--T-- RENAME USER old_name@host1 TO new_name@host1
RENAME USER delUser@localhost TO renamed1@localhost;

--T-- ALTER USER user1@host1 ACCOUNT LOCK|UNLOCK
ALTER USER renamed1@localhost ACCOUNT LOCK;

--T-- DROP USER [IF EXISTS] user1@host1
DROP USER IF EXISTS renamed1@localhost;

--T-- DROP ROLE [IF EXISTS] role1@host1
DROP ROLE IF EXISTS midPriviRole1@localhost, role2@localhost;