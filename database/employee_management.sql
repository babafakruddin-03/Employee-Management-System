-- Create the Employee Management database
CREATE DATABASE IF NOT EXISTS employee_management;

-- Select the database
USE employee_management;

-- Create the employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    joining_date DATE
);