CREATE DATABASE Restaurant;
USE Restaurant;

CREATE TABLE Category (
	Id				INT AUTO_INCREMENT PRIMARY KEY,
	CategoryName	VARCHAR(200) NOT NULL
);

CREATE TABLE Customer (
	Id					INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Full_Name			VARCHAR(200) NOT NULL,
    Phone				VARCHAR(20) NOT NULL,
    Number_people		INT NOT NULL,
    Arrive_time			DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Chef (
	Id				INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Full_Name		VARCHAR(200) NOT NULL,
	Email			VARCHAR(200) NOT NULL,
    Phone			VARCHAR(20) NOT NULL,
    Salary			FLOAT NOT NULL
);

CREATE TABLE Dishes (
	Id				INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Dish_name		VARCHAR(200) NOT NULL,
	Price			FLOAT NOT NULL,
	Status			VARCHAR(9) NOT NULL,
		CHECK(status = "Sold out" OR status = "Remaining"),
    Description		LONGTEXT,
    CategoryId		INT NOT NULL REFERENCES Category(Id),
    ChefId			INT NOT NULL REFERENCES Chef(Id)
);

CREATE TABLE Ordering (
	Id				INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	CustomerId		INT NOT NULL REFERENCES Customer(Id)
);

CREATE TABLE Dishes_Ordering (
	Id				INT  NOT NULL AUTO_INCREMENT PRIMARY KEY,
	DishesId		INT NOT NULL REFERENCES Dishes(Id),
    OrderingId		INT NOT NULL REFERENCES Ordering(Id),
	Quantity		INT NOT NULL,
    Price			FLOAT NOT NULL
);

CREATE TABLE Ingredient (
	Id					INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Ingredient_name		VARCHAR(200) NOT NULL,
    Description			LONGTEXT
);

CREATE TABLE Dishes_Ingredient (
	Id					INT  NOT NULL AUTO_INCREMENT PRIMARY KEY,
	DishesId			INT NOT NULL REFERENCES Dishes(Id),
    IngredientId		INT NOT NULL REFERENCES Ingredient(Id)
);

CREATE TABLE Comment (
	Id					INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	CustomerId			INT NOT NULL REFERENCES Customer(Id),
	DishesId			INT NOT NULL REFERENCES Dishes(Id),
	CreatedAt			DATETIME DEFAULT CURRENT_TIMESTAMP,
	Content				LONGTEXT,
	Rate				FLOAT DEFAULT 0
);

INSERT INTO Category (CategoryName)
	VALUES ('Mon chinh'), ('Nuoc uong');
INSERT INTO Customer (Full_Name, Phone, Number_people, Arrive_time)
	VALUES ('Son','0855118693',3 ,'12-01-16'),
			('Hieu','123456789',1 ,'12-01-16'),
			('Hoa','01697637337',5 ,'12-01-16');
INSERT INTO Chef (Full_Name, Email, Phone, Salary)
	VALUES ('Chuong','chuong@gmail.com','0983550162',5000),
			('Long','chuong@gmail.com','0983550162',5000),
			('Hack','chuong@gmail.com','0983550162',5000);
INSERT INTO Dishes (Dish_name, Price, Status, Description, CategoryId, ChefId)
	VALUES('Thit cho', 3000, 'Remaining', 'Rat ngon', 1, 1),
			('Thit lon', 3000, 'Remaining', 'Rat ngon', 1, 2),
            ('Thit bo', 3000, 'Remaining', 'Rat ngon', 1, 1);
INSERT INTO Ordering (CustomerId)
	VALUES(1), (2), (3);
INSERT INTO Dishes_Ordering (DishesId, OrderingId, Quantity,Price)
	VALUES(1,1,3,9000), (2,2,4,12000);
INSERT INTO Ingredient (Ingredient_name, Description)
	VALUES('Chan', 'ngan'), ('Long', 'ngon'), ('Doi', 'chan');
INSERT INTO Dishes_Ingredient (DishesId, IngredientId)
	VALUES(1, 1), (2, 2);
INSERT INTO Comment (CustomerId, DishesId, CreatedAt, Content, Rate)
	VALUES(1,2,'12-01-16','good job', 5),
			(2,3,'12-01-16','very good job', 4);
            
SELECT * FROM Category;
SELECT * FROM Customer;
SELECT * FROM Chef;
SELECT * FROM Dishes;
SELECT * FROM Ordering;
SELECT * FROM Dishes_Ordering;
SELECT * FROM Ingredient;
SELECT * FROM Dishes_Ingredient;
SELECT * FROM Comment




