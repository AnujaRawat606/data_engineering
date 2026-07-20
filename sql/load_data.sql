INSERT INTO customers
(customer_id, first_name, last_name, email, country)
VALUES
(1, 'Anna', 'Schmidt', 'anna@email.com', 'Germany'),
(2, 'John', 'Smith', 'john@email.com', 'USA'),
(3, 'Maria', 'Garcia', 'maria@email.com', 'Spain');

INSERT INTO orders
(order_id, customer_id, product_id, quantity, order_date)
VALUES
(5001, 1, 101, 1, '2026-01-10'),
(5002, 2, 102, 2, '2026-01-11'),
(5003, 1, 103, 3, '2026-01-12');

INSERT INTO products
(product_id, product_name, category, price)
VALUES
(101, 'Laptop', 'Electronics', 1200.00),
(102, 'Headphones', 'Electronics', 150.00),
(103, 'Coffee Mug', 'Home', 15.00);
