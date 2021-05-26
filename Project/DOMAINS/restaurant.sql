drop database resma;
CREATE DATABASE resma;
USE resma;
CREATE TABLE Customer (
	Id					INT NOT NULL  PRIMARY KEY,
	Full_Name			VARCHAR(200) NOT NULL ,
    Phone				VARCHAR(20) NOT NULL,
    Number_people		INT NOT NULL,
    Arrive_time			TEXT NOT NULL
);

CREATE TABLE Dishes (
	Id				INT NOT NULL  PRIMARY KEY,
	Dish_name		VARCHAR(200) NOT NULL,
	Price			FLOAT NOT NULL
);

CREATE TABLE Ordering (
	Id				INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	CustomerId		INT NOT NULL REFERENCES Customer(Id)
);

CREATE TABLE Dishes_Ordering (
	Id				INT  NOT NULL AUTO_INCREMENT PRIMARY KEY,
	DishesId		INT NOT NULL REFERENCES Dishes(Id),
    OrderingId		INT NOT NULL REFERENCES Ordering(Id),
	Quantity		INT NOT NULL
);

INSERT INTO Dishes(Id,Dish_name,Price)
VALUES (1,'Buri',250),
       (2,'Grilled cod fish',360),
       (3,'Herring fish',250),
       (4,'Karikari',175),
       (5, 'Saba', 245),
       (6,'Salmon',325),
       (7,'Snapper',185),
       (8,'Chankonabe',80);
select * from Customer;
select * from Dishes;

select COUNT(Id) 
from Dishes;