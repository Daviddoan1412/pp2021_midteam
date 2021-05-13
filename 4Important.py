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

    sql_create_dishes_table = """CREATE TABLE IF NOT EXISTS Dishes (
    Id				INT NOT NULL PRIMARY KEY,
    Dish_name		VARCHAR(200) NOT NULL,
    Price			FLOAT NOT NULL,
    Status			VARCHAR(9) NOT NULL
        CHECK(status = "Sold out" OR status = "Remaining"),
    Description		LONGTEXT,
    CategoryId		INT NOT NULL,
    FOREIGN KEY (CategoryId) REFERENCES Category (Id)
);"""

    sql_create_ordering_table = """CREATE TABLE IF NOT EXISTS Ordering (
    Id				INT NOT NULL PRIMARY KEY,
    CustomerId		INT NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Customer (Id)
);"""

    sql_create_dishes_ordering_table = """CREATE TABLE IF NOT EXISTS Dishes_Ordering (
    Id				INT  NOT NULL PRIMARY KEY,
    DishesId		INT NOT NULL,
    OrderingId		INT NOT NULL,
    Quantity		INT NOT NULL,
    FOREIGN KEY (DishesId) REFERENCES Dishes (Id),
    FOREIGN KEY (OrderingId) REFERENCES Ordering (Id)
);"""

    database = r"C:\Users\dmx\Desktop\python\Midterm\Python_SQLite.db"
    con = create_connection(database)
    if con is not None:
        create_table(con, sql_create_category_table)
        create_table(con, sql_create_customer_table)
        create_table(con, sql_create_dishes_table)
        create_table(con, sql_create_ordering_table)
        create_table(con, sql_create_dishes_ordering_table)

    else:
        print("Error!!! Cannot create the database connection")



if __name__ == '__main__':
    main()