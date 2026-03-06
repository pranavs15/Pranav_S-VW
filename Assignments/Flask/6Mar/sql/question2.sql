
CREATE DATABASE RetailDB;


USE RetailDB;



CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount FLOAT
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price FLOAT
);

CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT
);



INSERT INTO Customers VALUES
(1,'Anjali ','Mumbai'),
(2,'Vikram ','Ahmedabad'),
(3,'Neha ','Delhi'),
(4,'Suresh ','Chennai'),
(5,'Ramesh ','Kolkata'),
(6,'Pooja ','Pune');

INSERT INTO Orders VALUES
(101,1,'2023-01-10',5000),
(102,1,'2023-02-15',3000),
(103,1,'2023-03-20',2000),
(104,1,'2023-04-25',1500),
(105,2,'2023-01-05',7000),
(106,2,'2023-02-18',4000),
(107,3,'2023-03-01',2500),
(108,4,'2023-04-12',6000);

INSERT INTO Products VALUES
(1,'Laptop',50000),
(2,'Smartphone',20000),
(3,'Headphones',3000),
(4,'Keyboard',1500);

INSERT INTO Order_Items VALUES
(1,101,1,1),
(2,101,3,2),
(3,102,2,1),
(4,103,4,1),
(5,104,3,2),
(6,105,1,1),
(7,106,2,1),
(8,107,3,3),
(9,108,1,1);


--  Find customers who placed more than 3 orders.


SELECT c.customer_id, c.name, COUNT(o.order_id) AS total_orders
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 3;


--  Find the top 5 customers by total spending.


SELECT c.customer_id, c.name, SUM(o.total_amount) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 5;


-- Display the most ordered product.


SELECT p.product_id, p.product_name, SUM(oi.quantity) AS total_quantity
FROM Products p
JOIN Order_Items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity DESC
LIMIT 1;


--  Find customers who never placed an order.


SELECT customer_id, name
FROM Customers
WHERE customer_id NOT IN (
SELECT customer_id FROM Orders
);


--  Calculate the total revenue generated each month.


SELECT DATE_FORMAT(order_date,'%Y-%m') AS month,
SUM(total_amount) AS total_revenue
FROM Orders
GROUP BY month
ORDER BY month;