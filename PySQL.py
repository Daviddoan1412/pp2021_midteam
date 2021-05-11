import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    #Create a connection to SQLite database
    con = None
    try:
        con = sqlite3.connect(db_file)
        return con
    except Error as E:
        print(E)

    return con

def create_table(con, sql_table):
    #Create a table from sql_table statement
    try:
        c = con.cursor()
        c.execute(sql_table)
    except Error as E:
        print(E)

def main():
    database = r"C:\Users\dmx\Desktop\python\Midterm\Python_SQLite.db"

    sql_create_category_table = """CREATE TABLE IF NOT EXISTS  Category (
    Id				INT PRIMARY KEY,
    CategoryName	VARCHAR(200) NOT NULL
);"""

    sql_create_customer_table = """CREATE TABLE IF NOT EXISTS Customer (
    Id					INT NOT NULL PRIMARY KEY,
    Full_Name			VARCHAR(200) NOT NULL,
    Phone				VARCHAR(20) NOT NULL,
    Number_people		INT NOT NULL,
    Arrive_time			DATETIME DEFAULT CURRENT_TIMESTAMP
);"""
    sql_create_chef_table = """CREATE TABLE IF NOT EXISTS Chef (
    Id				INT NOT NULL PRIMARY KEY,
    Full_Name		VARCHAR(200) NOT NULL,
    Email			VARCHAR(200) NOT NULL,
    Phone			VARCHAR(20) NOT NULL,
    Salary			FLOAT NOT NULL
);"""

    sql_create_dishes_table = """CREATE TABLE IF NOT EXISTS Dishes (
    Id				INT NOT NULL PRIMARY KEY,
    Dish_name		VARCHAR(200) NOT NULL,
    Price			FLOAT NOT NULL,
    Status			VARCHAR(9) NOT NULL
        CHECK(status = "Sold out" OR status = "Remaining"),
    Description		LONGTEXT,
    CategoryId		INT NOT NULL REFERENCES Category(Id),
    ChefId			INT NOT NULL REFERENCES Chef(Id)
);"""

    sql_create_ordering_table = """CREATE TABLE IF NOT EXISTS Ordering (
    Id				INT NOT NULL PRIMARY KEY,
    CustomerId		INT NOT NULL REFERENCES Customer(Id)
);"""

    sql_create_dishes_ordering_table = """CREATE TABLE IF NOT EXISTS Dishes_Ordering (
    Id				INT  NOT NULL PRIMARY KEY,
    DishesId		INT NOT NULL REFERENCES Dishes(Id),
    OrderingId		INT NOT NULL REFERENCES Ordering(Id),
    Quantity		INT NOT NULL,
    Price			FLOAT NOT NULL
);"""

    sql_create_ingredient_table = """CREATE TABLE IF NOT EXISTS Ingredient (
    Id					INT NOT NULL PRIMARY KEY,
    Ingredient_name		VARCHAR(200) NOT NULL,
    Description			LONGTEXT
);"""

    sql_create_dishes_ingredient_table = """CREATE TABLE IF NOT EXISTS Dishes_Ingredient (
    Id					INT  NOT NULL PRIMARY KEY,
    DishesId			INT NOT NULL REFERENCES Dishes(Id),
    IngredientId		INT NOT NULL REFERENCES Ingredient(Id)
);"""

    sql_create_comment_table = """CREATE TABLE IF NOT EXISTS Comment (
    Id					INT NOT NULL PRIMARY KEY,
    CustomerId			INT NOT NULL REFERENCES Customer(Id),
    DishesId			INT NOT NULL REFERENCES Dishes(Id),
    CreatedAt			DATETIME DEFAULT CURRENT_TIMESTAMP,
    Content				LONGTEXT,
    Rate				FLOAT DEFAULT 0
);"""

    con = create_connection(database)
    if con is not None:
        create_table(con, sql_create_category_table)
        create_table(con, sql_create_customer_table)
        create_table(con, sql_create_chef_table)
        create_table(con, sql_create_dishes_table)
        create_table(con, sql_create_ordering_table)
        create_table(con, sql_create_dishes_ordering_table)
        create_table(con, sql_create_ingredient_table)
        create_table(con, sql_create_dishes_ingredient_table)
        create_table(con, sql_create_comment_table)

    else:
        print("Error!!! Cannot create the database connection")


    


if __name__ == '__main__':
    main()