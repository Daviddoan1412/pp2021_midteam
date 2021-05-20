from tkinter import*
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
import random
import time
import mysql.connector

# ====================================== set current time ======================================#

localtime=time.asctime(time.localtime(time.time()))

# ====================================== connection database ======================================#
mydb = mysql.connector.connect(
  host="127.0.0.2",
  user="root",
  password="855182",
  database="resma"
)

mycursor = mydb.cursor()


# ====================================== Set screen tkinter (interface) ======================================#
root = Tk()
root.title('Restaurant Management')
root.geometry("1400x800")


# =============================== Function to add, update, show, delete of Database =============================== #
def addCUS():

    a=txtFull_Name.get()
    b=txtPhone.get()
    c=txtNumber_people.get()
    d=txtArrive_time.get()

    try:
        sql = "INSERT INTO Customer (Full_Name, Phone,Number_people,Arrive_time) VALUES (%s, %s,%s,%s)"
        val = (a, b, c, d)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Insert Customer successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()


def updateCUS():

    a=txtFull_Name.get()
    b=txtPhone.get()
    c=txtNumber_people.get()
    d=txtArrive_time.get()

    try:
        sql = "UPDATE Customer SET  Phone=%s,Number_people=%s,Arrive_time=%s WHERE Id=%s"
        val = (a, b, c, d)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Update Customer successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()


def deleteCUS():

    a = txtFull_Name.get()
    b = txtPhone.get()
    c = txtNumber_people.get()
    d = txtArrive_time.get()

    try:
        sql = "DELETE FROM Customer WHERE Full_Name = %s"
        val=(a,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Delete Customer successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()


def addPRODUCT():

    a=txt_id.get()
    b = txtDish_Name.get()
    c = txtPrice.get()

    try:
        sql = "INSERT INTO Dishes (Id,Dish_name, Price) VALUES (%s, %s,%s)"
        val = (a, b,c)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Insert product successfully")
    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()

def updatePRODUCT():

    a = txt_id.get()
    b= txtDish_Name.get()
    c = txtPrice.get()

    try:
        sql = "UPDATE Dishes SET Dish_name= %s, Price= %s WHERE Id= %s"
        val = (a,b,c)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Update product successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()

def deletePRODUCT():

    a = txt_id.get()
    b = txtDish_Name.get()
    c = txtPrice.get()

    try:
        sql = "DELETE FROM Dishes WHERE Id = %s"
        val=(a,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Delete Disher successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()

def addOrdering():
    global Id
    global CustomerId

    a=Id.get()
    b=CustomerId.get()

    try:
        sql = "INSERT INTO Ordering (CustomerId,) VALUES (%s)"
        val = (b,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Insert Ordering successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()

def updateOrdering():
    global Id
    global CustomerId

    a = Id.get()
    b = CustomerId.get()

    try:
        sql = "UPDATE Ordering SET CustomerId= %s  WHERE Id= %s"
        val = (a, b)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Update Ordering successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()

def deleteOrdering():
    global Id

    a = Id.get()
    try:
        sql = "DELETE FROM Ordering WHERE Id = %s"
        val=(a,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Delete Ordering successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()


def add_Dishes_Ordering():
    global Id
    global DishesId
    global OrderingId
    global Quantity

    a = Id.get()
    b = DishesId.get()
    c = OrderingId.get()
    d = Quantity.get()

    try:
        sql = "INSERT INTO Dishes_Ordering (DishesId, OrderingId, Quantity) VALUES (%s, %s, %s)"
        val = (b, c, d)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Insert Dishes_Ordering successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()


def delete_Dishes_Ordering():
    global Id

    a = Id.get()
    try:
        sql = "DELETE FROM Dishes_Ordering WHERE Id = %s"
        val = (a,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Delete Dishes_Ordering successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()

def update_Dishes_Ordering():
    global Id
    global DishesId
    global OrderingId
    global Quantity

    a = Id.get()
    b = DishesId.get()
    c = OrderingId.get()
    d = Quantity.get()

    try:
        sql = "UPDATE Dishes_Ordering SET DishesId= %s, OrderingId= %s, Quantity= %s WHERE Id= %s"
        val = (b, c, d)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Update Dishes_Ordering successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()

def dis_customer():

    secondWindow = tk.Tk()
    secondWindow.geometry('1250x400')
    secondWindow.title("Customer management")

    appLabel = tk.Label(secondWindow,
                        text="Customer",
                        fg="#06a099",
                        width=40)

    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four", "five")

    tree.heading("one", text="Id")
    tree.heading("two", text="Full Name")
    tree.heading("three", text="Phone")
    tree.heading("four", text="Number people")
    tree.heading("five", text="Arrive time")

    sql ="SELECT * FROM Customer;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    i = 0
    for row in myresult:
        tree.insert('', i, text="Customer " + str(row[0]),
                    values=(row[0], row[1], row[2], row[3], row[4]))
        i = i + 1
    tree.pack()
    secondWindow.mainloop()

def Menu():

    secondWindow = tk.Tk()
    secondWindow.geometry('1000x400')
    secondWindow.title("Dishes price")

    appLabel = tk.Label(secondWindow,
                        text="Menu",
                        fg="#06a099",
                        width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three")

    tree.heading("one", text="Id")
    tree.heading("two", text="Dishes Name")
    tree.heading("three", text="Price")

    sql ="SELECT * FROM Dishes;"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    i = 0
    for row in myresult:
        tree.insert('', i, text="Dish " + str(row[0]),
                    values=(row[0], row[1], row[2]))
        i = i + 1
    tree.pack()
    secondWindow.mainloop()

def Exit():

    exit_program = messagebox.askyesno(
        title='Restaurant Management System',
        message='Confirm if you want to exit program?')
    if exit_program > 0:
        root.destroy()
    else:
        return None

def Reset():

    txtFull_Name.delete(0, END)
    txtPhone.delete(0, END)
    txtNumber_people.delete(0, END)
    txtArrive_time.delete(0, END)

    txtDish_Name.delete(0, END)
    txtPrice.delete(0, END)
    txt_id.delete(0, END)

    txt_reference.delete(0, END)
    txt_Buri.delete(0, END)
    txt_Grilled_cod_fish.delete(0, END)
    txt_Herring_fish.delete(0, END)
    txt_karikari.delete(0, END)
    txt_Saba.delete(0, END)

    txt_Salmon.delete(0, END)
    txt_Snapper.delete(0, END)
    txt_Chankonabe.delete(0, END)
    txt_Cost.delete(0, END)
    txt_Total.delete(0, END)
    txt_Services.delete(0, END)

# ====================================== initial variable ======================================#

order_nu = StringVar()
Buri = StringVar()
Grilled_cod_fish = StringVar()
Herring_fish = StringVar()
karikari = StringVar()
Saba = StringVar()
Salmon = StringVar()
Snapper = StringVar()
Chankonabe = StringVar()
Cost = StringVar()
Services = StringVar()
Total = StringVar()


def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    order_nu.set(randomRef)

    dist_1= float(txt_Buri.get())
    dist_2= float(txt_Grilled_cod_fish.get())
    dist_3= float(txt_Herring_fish.get())
    dist_4= float(txt_karikari.get())
    dist_5= float(txt_Saba.get())
    dist_6= float(txt_Salmon.get())
    dist_7= float(txt_Snapper.get())
    dist_8= float(txt_Chankonabe.get())


    Buri_price = dist_1*250
    Grilled_cod_fish_price = dist_2*360
    Herring_fish_price = dist_3*250
    Karikari_price = dist_4*175
    Saba_price = dist_5*245
    Salmon_price = dist_6*325
    Snapper_price = dist_7*185
    Chankonabe_price = dist_8*80


    Totalcost=(Buri_price + Grilled_cod_fish_price + Herring_fish_price
               + Karikari_price + Saba_price + Salmon_price + Snapper_price + Chankonabe_price)
    Service = ((Buri_price + Grilled_cod_fish_price +
                Herring_fish_price + Karikari_price + Saba_price +
                Salmon_price + Snapper_price + Chankonabe_price)*0.1)
    TotalOveraLL = str(Totalcost + Service), "$"

    Services.set(Service)
    Cost.set(Totalcost)
    Total.set(TotalOveraLL)


# ====================================== Set gird layout ======================================#

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

# ===================================== Display table ordering =====================================#

lbl_reference = Label(rightframe1,
                      font=('aria', 16, 'bold italic'),
                      text="Order No.",
                      fg="orchid3",
                      bd=10,
                      anchor='w')
lbl_reference.grid(row=0, column=1)


txt_reference = Entry(rightframe1,
                      font=('ariel', 16, 'bold italic'),
                      textvariable=order_nu,
                      bd=6,
                      insertwidth=4,
                      bg="white",
                      justify='right')
txt_reference.grid(row=0,column=2)


lbl_Buri = Label(rightframe1,
                 font=('aria', 16, 'bold italic'),
                 text="Buri",
                 fg="green",
                 bd=10,
                 anchor='w')
lbl_Buri.grid(row=1, column=0)


txt_Buri = Entry(rightframe1,
                 font=('ariel', 16, 'bold italic'),
                 textvariable=Buri,
                 bd=6,
                 insertwidth=4,
                 bg="white",
                 justify='right',
                 state=NORMAL)
txt_Buri.grid(row=1, column=1)


lbl_Grilled_cod_fish = Label(rightframe1,
                             font=('aria', 16, 'bold italic'),
                             text="Grilled cod fish ",
                             fg="green",
                             bd=10,
                             anchor='w')
lbl_Grilled_cod_fish.grid(row=2, column=0)


txt_Grilled_cod_fish = Entry(rightframe1,
                             font=('ariel', 16, 'bold italic'),
                             textvariable = Grilled_cod_fish,
                             bd=6,
                             insertwidth=4,
                             bg="white",
                             justify='right')
txt_Grilled_cod_fish.grid(row=2, column=1)


lbl_Herring_fish = Label(rightframe1,
                         font=('aria', 16, 'bold italic'),
                         text="Herring fish",
                         fg="green",
                         bd=10,
                         anchor='w')
lbl_Herring_fish.grid(row=3, column=0)


txt_Herring_fish = Entry(rightframe1,
                         font=('ariel', 16, 'bold italic'),
                         textvariable=Herring_fish,
                         bd=6,
                         insertwidth=4,
                         bg="white",
                         justify='right')
txt_Herring_fish.grid(row=3, column=1)


lbl_karikari = Label(rightframe1,
                     font=('aria', 16, 'bold italic'),
                     text="Karikari",
                     fg="green",
                     bd=10,
                     anchor='w')
lbl_karikari.grid(row=4, column=0)


txt_karikari = Entry(rightframe1,
                     font=('ariel', 16, 'bold italic'),
                     textvariable=karikari,
                     bd=6,
                     insertwidth=4,
                     bg="white",
                     justify='right')
txt_karikari.grid(row=4, column=1)


lbl_Saba = Label(rightframe1,
                 font=('aria', 16, 'bold italic'),
                 text="Saba",
                 fg="green",
                 bd=10,
                 anchor='w')
lbl_Saba.grid(row=1, column=2)


txt_Saba = Entry(rightframe1,
                 font=('ariel', 16, 'bold italic'),
                 textvariable=Saba,
                 bd=6,
                 insertwidth=4,
                 bg="white",
                 justify='right')
txt_Saba.grid(row=1, column=3)


lbl_Salmon = Label(rightframe1,
                   font=('aria', 16, 'bold italic'),
                   text="Salmon",
                   fg="green",
                   bd=10,
                   anchor='w')
lbl_Salmon.grid(row=2, column=2)


txt_Salmon = Entry(rightframe1,
                   font=('ariel', 16, 'bold italic'),
                   textvariable=Salmon,
                   bd=6,
                   insertwidth=4,
                   bg="white",
                   justify='right')
txt_Salmon.grid(row=2, column=3)


lbl_Snapper = Label(rightframe1,
                    font=('aria', 16, 'bold italic'),
                    text="Snapper",
                    fg="green",
                    bd=10,
                    anchor='w')
lbl_Snapper.grid(row=3, column=2)


txt_Snapper = Entry(rightframe1,
                    font=('ariel', 16,'bold italic'),
                    textvariable=Snapper,
                    bd=6,
                    insertwidth=4,
                    bg="white",
                    justify='right')
txt_Snapper.grid(row=3, column=3)


lbl_Chankonabe = Label(rightframe1,
                       font=('aria',16, 'bold italic' ),
                       text="Chankonabe",
                       fg="green",
                       bd=10,
                       anchor='w')
lbl_Chankonabe.grid(row=4,column=2)


txt_Chankonabe = Entry(rightframe1,
                       font=('ariel', 16, 'bold italic'),
                       textvariable=Chankonabe,
                       bd=6,insertwidth=4,
                       bg="white",
                       justify='right')
txt_Chankonabe.grid(row=4, column=3)

# ===================================== Calculate cost =====================================#

lbl_Cost = Label(rightframe2,
                 font=('aria', 16, 'bold italic'),
                 text="Cost",
                 fg="orchid3",
                 bd=10,
                 anchor='w')
lbl_Cost.grid(row=0, column=1)


txt_Cost = Entry(rightframe2,
                 font=('ariel', 16, 'bold italic'),
                 textvariable=Cost,
                 bd=6,
                 insertwidth=4,
                 bg="white",
                 justify='right')
txt_Cost.grid(row=0, column=2)


lbl_Services = Label(rightframe2,
                     font=('aria', 16, 'bold italic'),
                     text="Services",
                     fg="orchid3",
                     bd=10,
                     anchor='w')
lbl_Services.grid(row=1, column=1)


txt_Services = Entry(rightframe2,
                     font=('ariel', 16, 'bold italic'),
                     textvariable=Services,
                     bd=6,
                     insertwidth=4,
                     bg="white",
                     justify='right')
txt_Services.grid(row=1, column=2)


lbl_Total = Label(rightframe2,
                  font=('aria', 16, 'bold italic'),
                  text="Total",
                  fg="red",
                  bd=10,
                  anchor='w')
lbl_Total.grid(row=2, column=1)


txt_Total = Entry(rightframe2,
                  font=('ariel', 16, 'bold italic'),
                  textvariable=Total,
                  bd=6,
                  insertwidth=4,
                  bg="white",
                  justify='right')
txt_Total.grid(row=2, column=2)

# ===================================== Set logo_left for restaurant =====================================#

load_banner= Image.open("./images/banner.jpg")
render_banner = ImageTk.PhotoImage(load_banner)
img_banner = Label(bottomFrame, image=render_banner, anchor=NW)
img_banner.place(x=15, y=400)

# ===================================== List button option for user chooses =====================================#

btnAdd = Button(bottomFrame,
                bd=4,
                font=('arial', 13, 'bold'),
                width=13,
                height=3,
                text='Add Customer',
                command=addCUS)
btnAdd.grid(row=0, column=1, padx=4, pady=1)


btnAddDish= Button(bottomFrame,
                   bd=4,
                   font=('arial', 13, 'bold'),
                   width=13,
                   height=3,
                   text='Add Dish',
                   command=addPRODUCT)
btnAddDish.grid(row=0, column=2, padx=4, pady=1)


btnDisCus = Button(bottomFrame,
                   bd=4,
                   font=('arial', 13, 'bold'),
                   width=15,
                   height=3,
                   text='Display Cus',
                   command= dis_customer)
btnDisCus.grid(row=0, column=3, padx=4, pady=1)


btnMenu = Button(bottomFrame,
                 bd=4,
                 font=('arial', 13, 'bold'),
                 width=13,
                 height=3,
                 text='Menu',
                 command= Menu)
btnMenu.grid(row=0, column=4, padx=4, pady=1)


btnUpdate_dish = Button(bottomFrame,
                        bd=4,
                        font=('arial', 13, 'bold'),
                        width=13,
                        height=3,
                        text='DeleteDish',
                        command= deletePRODUCT)
btnUpdate_dish.grid(row=0, column=5, padx=4, pady=1)


btnUpdate_Cus = Button(bottomFrame,
                        bd=4,
                        font=('arial', 13, 'bold'),
                        width=13,
                        height=3,
                        text='DeleteCus',
                        command= deleteCUS)
btnUpdate_Cus.grid(row=0, column=6, padx=4, pady=1)

btnTotal = Button(bottomFrame,
                  bd=4,
                  font=('arial', 13, 'bold'),
                  width=13,
                  height=3,
                  text='Total',
                  command= Ref)
btnTotal.grid(row=0, column=7, padx=4, pady=1)


btnUpdate = Button(bottomFrame,
                   bd=4,
                   font=('arial', 13, 'bold'),
                   width=13,
                   height=3,
                   text='Reset',
                   command=Reset)
btnUpdate.grid(row=0, column=8, padx=4, pady=1)


btnUpdate = Button(bottomFrame,
                   bd=4, font=('arial', 13, 'bold'),
                   width=13,
                   height=3,
                   text='Exit',
                   command=Exit)
btnUpdate.grid(row=0, column=9, padx=4, pady=1)

if __name__ =='__main__':
    root.mainloop()