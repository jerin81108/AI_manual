-- ================================================
-- File: veera_college.sql
-- Description: College Database with Department and Student Tables
-- ================================================

CREATE DATABASE IF NOT EXISTS college;
USE college;

-- Create DEPARTMENT table
CREATE TABLE IF NOT EXISTS DEPARTMENT(
    DeptID   INT PRIMARY KEY,
    DeptName VARCHAR(20)
);

-- Create STUDENT table with FK reference to DEPARTMENT
CREATE TABLE IF NOT EXISTS STUDENT(
    StudentID INT PRIMARY KEY,
    Name      VARCHAR(20),
    DeptID    INT,
    FOREIGN KEY(DeptID) REFERENCES DEPARTMENT(DeptID)
);

-- Insert data into DEPARTMENT
INSERT INTO DEPARTMENT VALUES(1, 'CSE');

-- Insert data into STUDENT
INSERT INTO STUDENT VALUES(101, 'Ravi', 1);

-- Display all records
SELECT * FROM DEPARTMENT;
SELECT * FROM STUDENT;
