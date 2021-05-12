import sqlite3
from sqlite3 import Error



class delete:
    """Delete from category"""
    def delete_category(con, id, Categoryname):
        """
        Delete a task by category id, name,
        """
        print("You want to data from category with: \n")
        print("1. id! \n")
        print("2. Category name!\n")
        option = int(input("YOU CHOSE: "))
        if option == 1:
            print("Enter the id of Category:")
            sql = 'DELETE FROM Category WHERE id=?'
            c = con.cursor()
            c.execute(sql_table, (id,))
            con.commit()
        else:
            print("Enter the Name of Category:")
            sql = 'DELETE FROM Category WHERE Categoryname=?'
            c = con.cursor()
            c.execute(sql_table, (Categoryname,))
            con.commit()

    """Delete from Customer"""
    def delete_Customer(con, id, Full_name, Phone, Number_people, Arrive_time):
        """
        Delete a task by category id, name,
        """
        print("You want to delete data from Customer with: \n")
        print("1. id! \n")
        print("2. Full_name!\n")
        print("3. Phone!\n")
        print("4. Number_people!\n")
        print("5. Arrive_time!\n")
        option = int(input("YOU CHOSE: "))
        if option == 1:
            print("Enter the id of Customer:")
            sql = 'DELETE FROM Customer WHERE id=?'
            c = con.cursor()
            c.execute(sql_table, (id,))
            con.commit()
        if option == 2:
            print("Enter the Full_name of Customer:")
            sql = 'DELETE FROM Customer WHERE Full_name=?'
            c = con.cursor()
            c.execute(sql_table, (Full_name,))
            con.commit()
        if option == 3:
            print("Enter the Phone of Customer:")
            sql = 'DELETE FROM Customer WHERE Phone=?'
            c = con.cursor()
            c.execute(sql_table, (Phone,))
            con.commit()
        if option == 4:
            print("Enter the Number_people of Customer:")
            sql = 'DELETE FROM Customer WHERE Number_people=?'
            c = con.cursor()
            c.execute(sql_table, (Number_people,))
            con.commit()
        else:
            print("Enter the Arrive_time of Customer:")
            sql = 'DELETE FROM Customer WHERE Arrive_time=?'
            c = con.cursor()
            c.execute(sql_table, (Arrive_time,))
            con.commit()

    """Delete from chef table"""
    def delete_chef(con, id, Full_name, Phone, Email, Salary):
        """
        Delete a task by category id, name,
        """
        print("You want to delete data from Customer with: \n")
        print("1. id! \n")
        print("2. Full_name!\n")
        print("3. Phone!\n")
        print("4. Email!\n")
        print("5. Salary!\n")
        option = int(input("YOU CHOSE: "))
        if option == 1:
            print("Enter the id of Chef:")
            sql = 'DELETE FROM chef WHERE id=?'
            c = con.cursor()
            c.execute(sql_table, (id,))
            con.commit()
        if option == 2:
            print("Enter the Full_name of Chef:")
            sql = 'DELETE FROM chef WHERE Full_name=?'
            c = con.cursor()
            c.execute(sql_table, (Full_name,))
            con.commit()
        if option == 3:
            print("Enter the Phone of Chef:")
            sql = 'DELETE FROM chef WHERE Phone=?'
            c = con.cursor()
            c.execute(sql_table, (Phone,))
            con.commit()
        if option == 4:
            print("Enter the Email of Chef:")
            sql = 'DELETE FROM chef WHERE Email=?'
            c = con.cursor()
            c.execute(sql_table, (Email,))
            con.commit()
        else:
            print("Enter the Salary of Chef:")
            sql = 'DELETE FROM chef WHERE Salary=?'
            c = con.cursor()
            c.execute(sql_table, (Salary,))
            con.commit()

    """Delete from Disher table"""
    def delete_Disher(con, id, Diss_name, Price, Status, Description, CategoryId, ChefId):
        """
        Delete a task by category id, name,
        """
        print("You want to delete data from Disher with: \n")
        print("1. id! \n")
        print("2. Diss_name!\n")
        print("3. Price!\n")
        print("4. Status!\n")
        print("5. Description!\n")
        print("6. Category ID!\n")
        print("7. Chef ID!\n")
        option = int(input("YOU CHOSE: "))
        if option == 1:
            print("Enter the id of Disher:")
            sql = 'DELETE FROM Disher WHERE id=?'
            c = con.cursor()
            c.execute(sql_table, (id,))
            con.commit()
        if option == 2:
            print("Enter the Disher name of Disher:")
            sql = 'DELETE FROM Disher WHERE Disher_name=?'
            c = con.cursor()
            c.execute(sql_table, (Diss_name,))
            con.commit()
        if option == 3:
            print("Enter the Price of Disher:")
            sql = 'DELETE FROM Disher WHERE Price=?'
            c = con.cursor()
            c.execute(sql_table, (Price,))
            con.commit()
        if option == 4:
            print("Enter the Status of Disher:")
            sql = 'DELETE FROM Disher WHERE Status=?'
            c = con.cursor()
            c.execute(sql_table, (Status,))
            con.commit()
        if option == 5:
            print("Enter the id of Disher:")
            sql = 'DELETE FROM Disher WHERE Description=?'
            c = con.cursor()
            c.execute(sql_table, (Description,))
            con.commit()
        if option == 5:
            print("Enter the id of Disher:")
            sql = 'DELETE FROM Disher WHERE CategoryId=?'
            c = con.cursor()
            c.execute(sql_table, (CategoryId,))
            con.commit()
        else:
            print("Enter the id of Disher:")
            sql = 'DELETE FROM Disher WHERE Chefid=?'
            c = con.cursor()
            c.execute(sql_table, (ChefId,))
            con.commit()


