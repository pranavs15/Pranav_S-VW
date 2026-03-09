
CREATE DATABASE ECommerceDB;

USE ECommerceDB;


CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount FLOAT
);


INSERT INTO Orders VALUES
(101, 1, 1, 2, 4000),
(102, 1, 2, 1, 2000),
(103, 1, 3, 3, 4500),
(104, 2, 1, 1, 2000),
(105, 2, 2, 2, 4000),
(106, 2, 3, 1, 1500),
(107, 3, 1, 4, 8000),
(108, 3, 4, 2, 3000),
(109, 4, 2, 1, 2000),
(110, 5, 3, 5, 7500),
(111, 5, 4, 2, 3000),
(112, 5, 1, 1, 2000),
(113, 1, 4, 1, 1500),
(114, 1, 2, 2, 4000);


-- Find the total amount spent by each customer.

SELECT customer_id, SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id;


--  Find the number of orders placed by each customer.

SELECT customer_id, COUNT(order_id) AS total_orders
FROM Orders
GROUP BY customer_id;


--  Display customers who placed more than 3 orders.

SELECT customer_id, COUNT(order_id) AS total_orders
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;


-- Find customers whose total spending is greater than 10,000.

SELECT customer_id, SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id
HAVING SUM(total_amount) > 10000;


-- Find products whose total quantity sold is greater than 100.

SELECT product_id, SUM(quantity) AS total_quantity_sold
FROM Orders
GROUP BY product_id
HAVING SUM(quantity) > 100;