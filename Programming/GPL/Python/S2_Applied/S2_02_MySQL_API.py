
#   MySQL API

#T# database access with the MySQL API

#T# import the pymysql module
import pymysql

#T# create database object with pymysql.connect()
db1 = pymysql.connect("localhost","testUser","tUserP4$$","testdb")

#T# create database cursor with cursor() to travel the rows of a result set
cursor1 = db1.cursor()

#T# execute SQL statements in a try except block
try:

#T# execute an SQL statement with execute()
    cursor1.execute("SELECT VERSION()")

#T# fetch one row of the result set with fetchone()
    data1 = cursor1.fetchone()
    print("Gathered data is:",data1)

#T# execute more SQL statements
    cursor1.execute("DROP TABLE IF EXISTS EMPLOYEE")
    cursor1.execute("""CREATE TABLE EMPLOYEE (FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), INCOME FLOAT)""")
    cursor1.execute("""INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME,AGE,
                SEX,INCOME) VALUES ('fName1','lName1',25,'F',5000)""")
    cursor1.execute("SELECT * FROM EMPLOYEE")

#T# get the remaining rows in the result set with fetchall()
    data2 = cursor1.fetchall()
    print("Result set is:",data2)

    cursor1.execute("UPDATE EMPLOYEE SET AGE = AGE + 1")
    cursor1.execute("DELETE FROM EMPLOYEE WHERE AGE < 18")

#T# commit changes to the database with commit()
    db1.commit()
except:
#T# rollback changes to the database if there is an error with rollback()
    db1.rollback()

#T# close the database connection with close()
db1.close()