create table product(
        productId int PRIMARY KEY,
        productName varchar(255),
        description varchar(255),
        price int,
        quantityInStock int,
        type varchar(255));


create table electronics(
        productId INT PRIMARY KEY,
        brand varchar(255),
		warrantyPeriod int,
		FOREIGN KEY (productID) REFERENCES product(productID)
);

create table clothing(
        productId INT PRIMARY KEY,
        size varchar(255),
        color varchar(255),
	    FOREIGN KEY (productID) REFERENCES product(productID)
);

create table [user](
        userId int,
        username varchar(255),
        password varchar(255),
        role varchar(255)
);
