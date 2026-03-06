
CREATE DATABASE EmployeeAnalysisDB;


USE EmployeeAnalysisDB;


-- Create Table


CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);



INSERT INTO Employees VALUES
(1,'Rahul ','IT',70000),
(2,'Priya ','HR',50000),
(3,'Amit ','Finance',90000),
(4,'Sonal ','IT',60000),
(5,'Rohit ','Marketing',55000),
(6,'Karan ','Finance',85000),
(7,'Sneha ','HR',52000),
(8,'Arjun ','IT',75000);


-- Find employees whose salary is greater than the average salary of all employees.


SELECT emp_id, emp_name, salary
FROM Employees
WHERE salary > (
SELECT AVG(salary) FROM Employees
);


--  Find employees whose salary is greater than the average salary of their own department.


SELECT e.emp_id, e.emp_name, e.department, e.salary
FROM Employees e
WHERE salary >
(
SELECT AVG(salary)
FROM Employees
WHERE department = e.department
);


--  Find employees who earn the highest salary in their department.


SELECT emp_id, emp_name, department, salary
FROM Employees e
WHERE salary =
(
SELECT MAX(salary)
FROM Employees
WHERE department = e.department
);


--  Display employees who earn less than the highest salary in the company but more than the average salary.


SELECT emp_id, emp_name, salary
FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees)
AND salary > (SELECT AVG(salary) FROM Employees);


-- Find departments whose average salary is greater than the company’s average salary.


SELECT department, AVG(salary) AS dept_avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > (
SELECT AVG(salary) FROM Employees
);