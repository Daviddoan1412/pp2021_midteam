from tkinter import*
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import ImageTk,Image
import random
import time
import mysql.connector

localtime=time.asctime(time.localtime(time.time()))
root = Tk()
root.title('Restaurant Management')
root.geometry("1400x800")
class interface:
    mainframe = Frame(root)
    mainframe.grid()

    topframe = Frame(mainframe,
                 bd=10,
                 width=1500,
                 height=500,
                 padx=2,
                 relief=RIDGE)
    topframe.pack(side=TOP)

# ====================================== Set logo_left for restaurant ======================================#

    load= Image.open("./images/logo.png")
    render = ImageTk.PhotoImage(load)
    img = Label(topframe, image=render, anchor=NW)
    img.place(x=50, y=17)

    subtopframe = Frame(topframe,
                    bd=5,
                    width=800,
                    height=200,
                    padx=2,
                    relief=RIDGE)
    subtopframe.pack(side=TOP)

# ================================================= INFO TOP =================================================#
    lbl_info = Label(subtopframe,
                 font=('Helvetica', 30, 'bold'),
                 text="Restaurant Management System",
                 bg="slate gray",
                 fg="white",
                 bd=10,
                 anchor='center')

    lbl_info.grid(row=0, column=0)
    lbl_info = Label(subtopframe,
                 font=("Times", 24, "bold italic" ),
                 text=localtime,
                 bg="gainsboro",
                 fg="black",
                 anchor='center')
    lbl_info.grid(row=1, column=0)

    leftframe = Frame(topframe,
                  bd=5,
                  width=500,
                  height=500,
                  padx=2,
                  relief=RIDGE)
    leftframe.pack(side=LEFT)


    leftframe1 = Frame(leftframe,
                   bd=5,
                   width=500,
                   height=350,
                   padx=5,
                   relief=RIDGE)
    leftframe1.grid(row=0, column=0)


    leftframe2 = Frame(leftframe,
                   bd=5,
                   width=500,
                   height=150,
                   padx=3,
                   relief=RIDGE)
    leftframe2.grid(row=1, column=0)


    rightframe = Frame(topframe,
                   bd=5,
                   width=950,
                   height=500,
                   padx=2,
                   relief=RIDGE)
    rightframe.pack(side=RIGHT)

    rightframe1 = Frame(rightframe,
                    bd=5,
                    width=950,
                    height=350,
                    padx=5,
                    relief=RIDGE)
    rightframe1.grid(row=0, column=0)

    rightframe2 = Frame(rightframe,
                    bd=5,
                    width=950,
                    height=150,
                    padx=3,
                    relief=RIDGE)
    rightframe2.grid(row=1, column=0)


    bottomFrame = Frame(mainframe,
                    bd=10,
                    width=2000,
                    height=300,
                    padx=2,
                    relief=RIDGE)
    bottomFrame.pack(side=BOTTOM)

# get information of customer

    lblIdCus= Label(leftframe1,
                     font=('arial', 12, 'bold'),
                     text="CustomerId", padx=1)
    lblIdCus.grid(row=0, column=0, sticky=W)

    txtIdCus = Entry(leftframe1,
                     font=('arial', 12, 'bold'),
                     width=20)
    txtIdCus.grid(row=0, column=1, pady=3, padx=20)

    lblFull_Name = Label(leftframe1,
                     font=('arial', 12, 'bold'),
                     text="CustomerName", padx=1)
    lblFull_Name.grid(row=1, column=0, sticky=W)


    txtFull_Name = Entry(leftframe1,
                     font=('arial', 12, 'bold'),
                     width=20)
    txtFull_Name.grid(row=1, column=1, pady=3, padx=20)


    lblPhone = Label(leftframe1,
                 font=('arial', 12, 'bold'),
                 text="Phone", padx=1)
    lblPhone.grid(row=2, column=0, sticky=W)


    txtPhone = Entry(leftframe1,
                 font=('arial', 12, 'bold'),
                 width=20)
    txtPhone.grid(row=2, column=1, pady=3, padx=20)


    lblNumber_people = Label(leftframe1,
                         font=('arial', 12, 'bold'),
                         text="Number_people",
                         padx=1)
    lblNumber_people.grid(row=3, column=0, sticky=W)


    txtNumber_people = Entry(leftframe1,
                         font=('arial', 12, 'bold'),
                         width=20)
    txtNumber_people.grid(row=3, column=1, pady=3, padx=20)


    lblArrive_time = Label(leftframe1,
                       font=('arial', 12, 'bold'),
                       text="Arrive_time",
                       padx=1)
    lblArrive_time.grid(row=4, column=0, sticky=W)


    txtArrive_time = Entry(leftframe1,
                       font=('arial', 12, 'bold'),
                       width=20)
    txtArrive_time.grid(row=4, column=1, pady=3, padx=20)

# ===================================== Get information of dish =====================================#

    lbl_id= Label(leftframe2,
              font=('arial', 12, 'bold'),
              text="Id",
              padx=1)
    lbl_id.grid(row=9, column=0, sticky=W)


    txt_id = Entry(leftframe2,
               font=('arial', 12, 'bold'),
               width=20)
    txt_id.grid(row=9, column=1, pady=3, padx=20)


    lblDish_Name = Label(leftframe2,
                     font=('arial', 12, 'bold'),
                     text="Dish Name           ",
                     padx=1)
    lblDish_Name.grid(row=10, column=0, sticky=W)


    txtDish_Name = Entry(leftframe2,
                     font=('arial', 12, 'bold'),
                     width=20)
    txtDish_Name.grid(row=10, column=1, pady=3, padx=20)


    lblPrice = Label(leftframe2,
                 font=('arial', 12, 'bold'),
                 text="Price",
                 padx=1)
    lblPrice.grid(row=11, column=0, sticky=W)


    txtPrice = Entry(leftframe2,
                 font=('arial', 12, 'bold'),
                 width=20)
    txtPrice.grid(row=11, column=1, pady=3, padx=20)

