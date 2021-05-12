import sqlite3
from sqlite3 import Error



class delete:
# -----------------------------------------------------------------#

    """Delete from category"""
    def delete_category(con, id):
        """
        Delete a task by category id
        """
        sql = 'DELETE FROM Category WHERE Id=?'
        cur = con.cursor()
        cur.execute(sql, (id,))
        con.commit()

    """Delete all task from Category"""
    def delete_all_Category(con):
        sql = 'DELETE FROM Category?'
        cur = con.cursor()
        cur.execute(sql)
        con.commit()

#-----------------------------------------------------------------#

    """Delete from Customer"""
    def delete_Customer(con, id):
        """
        Delete a task by Customer id
        """
        sql = 'DELETE FROM Customer WHERE Id=?'
        cur = con.cursor()
        cur.execute(sql, (id,))
        con.commit()

    """Delete all task from Customer"""
    def delete_all_Customer(con):
        sql = 'DELETE FROM Customer?'
        cur = con.cursor()
        cur.execute(sql)
        con.commit()

#-----------------------------------------------------------------#

    def delete_Disher(con, id):
        """
        Delete a task by  Dishes id
        """
        sql = 'DELETE FROM Dishes WHERE Id=?'
        cur = con.cursor()
        cur.execute(sql, (id,))
        con.commit()


    """Delete all task from Disher"""
    def delete_all_Disher(con):
        sql = 'DELETE FROM Disher?'
        cur = con.cursor()
        cur.execute(sql)
        con.commit()


#-----------------------------------------------------------------#

    """Delete chef"""
    def delete_chef(con, id):
        """
        Delete a task by  Chef id
        """
        sql = 'DELETE FROM Chef WHERE Id=?'
        cur = con.cursor()
        cur.execute(sql, (id,))
        con.commit()


    """Delete all task from Chef"""

    def delete_all_Chef(con):
        sql = 'DELETE FROM Chef?'
        cur = con.cursor()
        cur.execute(sql)
        con.commit()

#-----------------------------------------------------------------#

    """Delete Ordering"""
    def delete_Ordering(con, id):
        """
        Delete a task by Ordering id
        """
        sql = 'DELETE FROM Ordering WHERE Id=?'
        cur = con.cursor()
        cur.execute(sql, (id,))
        con.commit()


    """Delete all task from Ordering"""
    def delete_all_Ordering(con):
        sql = 'DELETE FROM Ordering?'
        cur = con.cursor()
        cur.execute(sql)
        con.commit()

#-----------------------------------------------------------------#

    """Delete ordering table"""
    def delete_Dishes_Ordering(con, id):
        """
        Delete a task by Disher Ordering id
        """
        sql = 'DELETE FROM Dishes_Ordering WHERE Id=?'
        cur = con.cursor()
        cur.execute(sql, (id,))
        con.commit()

    """Delete all task from Chef"""
    def delete_all_Dishes_Ordering(con):
        sql = 'DELETE FROM Dishes_Ordering?'
        cur = con.cursor()
        cur.execute(sql)
        con.commit()