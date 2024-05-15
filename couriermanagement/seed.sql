INSERT INTO product (productId, productName, description, price, quantityInStock, type) 
VALUES 
    (1, 'Laptop', 'High-performance laptop', 1000, 10, 'Electronics'),
    (2, 'T-shirt', 'Cotton T-shirt', 20, 250, 'Clothing'),
    (3, 'Smartphone', 'Latest smartphone model', 800, 20, 'Electronics'),
	(4, 'Tops', 'Cotton Top', 30, 500, 'Clothing');

INSERT INTO electronics (productId,brand, warrantyPeriod, productID)
VALUES 
    (1,'Samsung', 2, 1),
	(3,'Apple', 1, 3);

INSERT INTO clothing (productId, size, color,productId)
VALUES 
    (2, 'M', 'Blue',2),
    (4, 'L', 'Red',4);

INSERT INTO [user] (userId, username, password, role)
VALUES 
    (1, 'john_doe', 'password123', 'Admin'),
    (2, 'jane_smith', 'qwerty456', 'User'),
	(3,'Karunya','hwfifi34','Admin');