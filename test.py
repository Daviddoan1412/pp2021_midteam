import sqlite3
from sqlite3 import Error

database = r"C:\Users\dmx\Desktop\python\Midterm\Python_SQLite.db"


class Databases:
    def create_connection(self, db_file):
        # Create a connection to SQLite database
        con = None
        try:
            con = sqlite3.connect(db_file)
            return con
        except Error as E:
            print(E)

        return con

    def create_table(self, con, sql_table):
        # Create a table from sql_table statement
        try:
            c = con.cursor()
            c.execute(sql_table)
        except Error as E:
            print(E)

    def main(self):
        sql_create_category_table = """CREATE TABLE IF NOT EXISTS  Category (

                                            Id				INT PRIMARY KEY,
                                            CategoryName	VARCHAR(200) NOT NULL

                                        );"""

        sql_create_customer_table = """CREATE TABLE IF NOT EXISTS Customer (

                                            Id					INT  PRIMARY KEY,
                                            Full_Name			VARCHAR(200) NOT NULL,
                                            Phone				VARCHAR(20) NOT NULL,
                                            Number_people		INT NOT NULL,
                                            Arrive_time			DATETIME DEFAULT CURRENT_TIMESTAMP

                                        );"""

        sql_create_chef_table = """CREATE TABLE IF NOT EXISTS Chef (

                                          Id				INT NOT NULL PRIMARY KEY,
                                          FullName		VARCHAR(200) NOT NULL,
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

                                          Id				INT PRIMARY KEY,
                                          CustomerId		INT NOT NULL,
                                          FOREIGN KEY (CustomerId) REFERENCES Customer (Id)
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

        con = Databases.create_connection(self, database)
        if con is not None:
            Databases.create_table(self, con, sql_create_category_table)
            Databases.create_table(self, con, sql_create_customer_table)
            Databases.create_table(self, con, sql_create_chef_table)
            Databases.create_table(self, con, sql_create_dishes_table)
            Databases.create_table(self, con, sql_create_ordering_table)
            Databases.create_table(self, con, sql_create_dishes_ordering_table)
            Databases.create_table(self, con, sql_create_ingredient_table)
            Databases.create_table(self, con, sql_create_dishes_ingredient_table)
            Databases.create_table(self, con, sql_create_comment_table)

        else:
            print("Error!!! Cannot create the database connection")

    # ----------------------------------INSERT------------------------------------------

    def insert_category_table(self, con, categorys):
        sql = '''INSERT INTO Category(Id,CategoryName)
                 VALUES(?,?) '''
        cur = con.cursor()
        cur.execute(sql, categorys)
        con.commit()
        return cur.lastrowid

    def insert_customer_table(self, con, custome):
        sql = '''INSERT INTO Customer(Full_Name, Phone ,Number_people,Arrive_time)
                 VALUES(?,?,?,?) '''
        cur = con.cursor()
        cur.execute(sql, custome)
        con.commit()
        return cur.lastrowid

    def insert__ordering_table(self, con, oderding):
        sql = '''INSERT INTO Ordering(CustomerId )
                 VALUES(?) '''
        cur = con.cursor()
        cur.execute(sql, oderding)
        con.commit()
        return cur.lastrowid

    def insert_chef_table(self, con, chef):
        sql = '''INSERT INTO Chef(Id, FullName	,Email,Phone,Salary )
                 VALUES(?,?,?,?,?) '''
        cur = con.cursor()
        cur.execute(sql, chef)
        con.commit()
        return cur.lastrowid

    def insert_dishes(self, con, dishes):
        sql = '''INSERT INTO  Dishes(Id,
                          Dish_name	,
                          Price)
                 VALUES(?,?,?) '''
        cur = con.cursor()
        cur.execute(sql, dishes)
        con.commit()
        return cur.lastrowid

    # # --------------------------------------------UPDATE-------------------------------------
    #
    # def update_category_table(con, category):
    #     sql = ''' UPDATE Category
    #               SET   Id	 = ? ,
    #                     CategoryName = ?
    #               WHERE Id = ?'''
    #     cur = con.cursor()
    #     cur.execute(sql, category)
    #     con.commit()
    #
    # def update_customer_table(con, customer):
    #
    #     sql = ''' UPDATE Customer
    #               SET  Id	 = ? ,
    #                    Full_Name	 = ? ,
    #                    Phone   =?,
    #                    Number_people   =?,
    #                    Arrive_time	=?
    #               WHERE Id = ?'''
    #     cur = con.cursor()
    #     cur.execute(sql, customer)
    #     con.commit()
    #
    # def update_ordering_table(con, oderding):
    #     sql = ''' UPDATE  Ordering
    #             SET     Id  = ?,
    #                     CustomerId = ?
    #             WHERE   Id =? '''
    #     cur = con.cursor()
    #     cur.execute(sql, oderding)
    #     con.commit()
    #
    # def updatee_chef_table(con, chef):
    #     sql = ''' UPDATE  Chef
    #             SET     Id  = ?,
    #                     FullName	=?,
    #                     Email	=?,
    #                     Phone	 =?,
    #                     Salary = ?
    #             WHERE   Id =? '''
    #     cur = con.cursor()
    #     cur.execute(sql, chef)
    #     con.commit()
    #
    # def update_dishes(con, dishes):
    #     sql = ''' UPDATE  Dishes
    #               SET     Id			=?,
    #                       Dish_name		=?,
    #                       Price	      =?
    #               WHERE   Id=? '''
    #     cur = con.cursor()
    #     cur.execute(sql, dishes)
    #     con.commit()


if __name__ == '__main__':
    start = Databases()
    con = start.create_connection(database)
    with con:
        categorys=('banana')
        categorys_1=('drink')
        start.insert_category_table(con,categorys)
        start.insert_category_table(con,categorys_1)

        custome=('longgg','0150366445','35','6:12 AM')
        CustomerId = start.insert_customer_table(con,custome)

        ordering=(CustomerId)
        start.insert__ordering_table(con,ordering)
    #
    #     Databases.update_category_table(con,(1,'daodaoshadg',1))
    #     Databases.update_customer_table(con,(1,'DaoHaiLong','0123456789','2','9:10',1))