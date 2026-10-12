# Employee Management System

## Project Overview

The Employee Management System is a Python application
that manages employee records using a MySQL database.

It allows users to add, view, search, update, and delete
employee information through a menu-driven interface.

## Technologies Used

- Python
- MySQL
- MySQL Connector for Python
- SQL
- VS Code

## Features

1. View all employees
2. Add a new employee
3. Search for an employee by ID
4. Update employee details
5. Delete an employee
6. Exit the application

## Database Design

Database: employee_management

Table: employees

Columns:
- employee_id
- employee_name
- email
- department
- salary
- joining_date

## Project Structure

Employee_Management_System/
- data/
  - employees.csv
- database/
  - employee_management.sql
- src/
  - db_connection.py
  - main.py
  - test_connection.py
- .gitignore
- README.md

## Installation and Setup

### 1. Install Python

Install Python if it is not already installed.

### 2. Install the MySQL Connector

Run the following command in your terminal:

python -m pip install mysql-connector-python

### 3. Set Up the Database

Open MySQL Workbench and execute the SQL commands
in database/employee_management.sql.

### 4. Configure the Database Connection

Configure the MySQL host, username, and password
locally. Never upload real passwords to GitHub.

### 5. Run the Application

From the project root directory, run:

python src/main.py

## Learning Outcomes

- Python functions
- SQL queries
- CRUD operations
- Python and MySQL connectivity
- Exception handling
- Database transactions