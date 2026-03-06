CREATE DATABASE CompanyDB;


USE CompanyDB;

-- Employees

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    joining_date DATE
);

INSERT INTO Employees VALUES
(1, 'Rahul ', 'IT', 70000, '2021-01-10'),
(2, 'Priya ', 'HR', 50000, '2020-03-15'),
(3, 'Amit ', 'Finance', 90000, '2019-07-20'),
(4, 'Sonal ', 'IT', 60000, '2022-05-01'),
(5, 'Rohit ', 'Marketing', 55000, '2021-11-11');

-- Projects
CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    start_date DATE,
    end_date DATE
);

INSERT INTO Projects VALUES
(1, 'Website Revamp', '2023-01-01', '2023-03-31'),
(2, 'Mobile App', '2023-02-01', '2023-06-30'),
(3, 'Finance Audit', '2023-03-01', '2023-05-30'),
(4, 'Marketing Campaign', '2023-04-01', '2023-08-31');

-- Employee_Project
CREATE TABLE Employee_Project (
    emp_id INT,
    project_id INT,
    hours_worked INT,
    rating FLOAT,
    PRIMARY KEY(emp_id, project_id)
);

INSERT INTO Employee_Project VALUES
(1, 1, 120, 4.5),
(1, 2, 150, 4.2),
(1, 3, 100, 4.8),
(2, 3, 80, 3.9),
(3, 3, 120, 4.9),
(4, 1, 100, 4.1),
(5, 4, 90, 4.0);


SELECT e.emp_id, e.emp_name
FROM Employees e
JOIN Employee_Project ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING COUNT(ep.project_id) > 2;

SELECT e.emp_id, e.emp_name, AVG(ep.rating) AS avg_rating
FROM Employees e
JOIN Employee_Project ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING AVG(ep.rating) > 4;

SELECT department, emp_name, salary
FROM Employees e1
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees e2
    WHERE e2.department = e1.department
);



SELECT emp_id, emp_name
FROM Employees
WHERE emp_id NOT IN (
    SELECT DISTINCT emp_id FROM Employee_Project
);


SELECT p.project_id, p.project_name, SUM(ep.hours_worked) AS total_hours
FROM Projects p
JOIN Employee_Project ep ON p.project_id = ep.project_id
GROUP BY p.project_id, p.project_name
ORDER BY total_hours DESC
LIMIT 1;

