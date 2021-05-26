from tkinter import*
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import ImageTk,Image
import random
import time
import mysql.connector
import INTERFACE
# ====================================== connection database ======================================#
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Lenovo",
  database="resma"
)

mycursor = mydb.cursor()

# =============================== Function to add, update, show, delete of Database =============================== #
class sqll:
    def addCUS(self):

        a=INTERFACE.interface.txtFull_Name.get()
        b=INTERFACE.interface.txtPhone.get()
        c=INTERFACE.interface.txtNumber_people.get()
        d=INTERFACE.interface.txtArrive_time.get()
        f = INTERFACE.interface.txtIdCus.get()

        if (a == "") | (b == "") | (c == "") | (d == "") | (f==""):
            messagebox.showinfo("ERROR", "Cannot add Customer")
        else:
            try:
                sql = "INSERT INTO Customer (Id,Full_Name, Phone,Number_people,Arrive_time) VALUES (%s, %s,%s,%s,%s)"
                val = (f,a, b, c, d)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("INFORMATION", "Insert Customer successfully")

            except EXCEPTION as e:
                print(e)
                mydb.rollback()
            mydb.close()


    def updateCUS(self):

        a=INTERFACE.interface.txtFull_Name.get()
        b=INTERFACE.interface.txtPhone.get()
        c=INTERFACE.interface.txtNumber_people.get()
        d=INTERFACE.interface.txtArrive_time.get()
        f = INTERFACE.interface.txtIdCus.get()

        if (a == "") | (b == "") | (c == "") | (d == "")| (f==""):
            messagebox.showinfo("ERROR", "Cannot update Customer")
        else:
            try:
                sql = "UPDATE Customer SET Full_Name=%s, Phone=%s,Number_people=%s,Arrive_time=%s WHERE Id=%s"
                val = (a, b, c, d, f)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("INFORMATION", "Update Customer successfully")

            except EXCEPTION as e:
                print(e)
                mydb.rollback()
            mydb.close()


    def deleteCUS(self):

        a = INTERFACE.interface.txtFull_Name.get()
        b = INTERFACE.interface.txtPhone.get()
        c = INTERFACE.interface.txtNumber_people.get()
        d = INTERFACE.interface.txtArrive_time.get()
        f = INTERFACE.interface.txtIdCus.get()

        if f == "" :
            messagebox.showinfo("ERROR", "Cannot Delete Customer")
        else:
            try:
                sql = "DELETE FROM Customer WHERE Id = %s"
                val=(f,)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("INFORMATION", "Delete Customer successfully")

            except EXCEPTION as e:
                print(e)
                mydb.rollback()
            mydb.close()


    def addPRODUCT(self):

        a=INTERFACE.interface.txt_id.get()
        b = INTERFACE.interface.txtDish_Name.get()
        c = INTERFACE.interface.txtPrice.get()
        if (a == "") | (b == "") | (c == ""):
            messagebox.showinfo("ERROR", "Cannot add product")
        else:
            try:
                sql = "INSERT INTO Dishes (Id,Dish_name, Price) VALUES (%s, %s,%s)"
                val = (a, b,c)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("INFORMATION", "Insert product successfully")
            except EXCEPTION as e:
                print(e)
                mydb.rollback()
            mydb.close()

    def updatePRODUCT(self):

        a = INTERFACE.interface.txt_id.get()
        b= INTERFACE.interface.txtDish_Name.get()
        c = INTERFACE.interface.txtPrice.get()
        if (a == "") | (b == "") | (c == ""):
            messagebox.showinfo("ERROR", "Cannot Update product")
        else:
            try:
                sql = "UPDATE Dishes SET Dish_name= %s, Price= %s WHERE Id= %s"
                val = (b,c,a)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("INFORMATION", "Update product successfully")

            except EXCEPTION as e:
                print(e)
                mydb.rollback()
            mydb.close()

    def deletePRODUCT(self):

        a = INTERFACE.interface.txt_id.get()
        b = INTERFACE.interface.txtDish_Name.get()
        c = INTERFACE.interface.txtPrice.get()
        if a == "":
            messagebox.showinfo("ERROR", "Cannot Delete product")
        else:
            try:
                sql = "DELETE FROM Dishes WHERE Id = %s"
                val=(a,)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("INFORMATION", "Delete product successfully")
            except EXCEPTION as e:
                print(e)
                mydb.rollback()
            mydb.close()

    def addOrdering(self):
        global Id
        global CustomerId

        a=Id.get()
        b=CustomerId.get()
        if b== "":
            messagebox.showinfo("ERROR", "Cannot add Ordering")
        else:
            try:
                sql = "INSERT INTO Ordering (CustomerId,) VALUES (%s)"
                val = (b,)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("INFORMATION", "Insert Ordering successfully")

            except EXCEPTION as e:
                print(e)
                mydb.rollback()
            mydb.close()

    def updateOrdering(self):
        global Id
        global CustomerId

        a = Id.get()
        b = CustomerId.get()
        if (b== "" )|(a ==""):
            messagebox.showinfo("ERROR", "Cannot Update Ordering")
        else:
            try:
                sql = "UPDATE Ordering SET CustomerId= %s  WHERE Id= %s"
                val = (a, b)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("INFORMATION", "Update Ordering successfully")

            except EXCEPTION as e:
                print(e)
                mydb.rollback()
            mydb.close()

    def deleteOrdering(self):
        global Id

        a = Id.get()
        if a== "":
            messagebox.showinfo("ERROR", "Cannot Delete Ordering")
        else:
            try:
                sql = "DELETE FROM Ordering WHERE Id = %s"
                val=(a,)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("INFORMATION", "Delete Ordering successfully")

            except EXCEPTION as e:
                print(e)
                mydb.rollback()
            mydb.close()


    def add_Dishes_Ordering(self):
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
            messagebox.showinfo("INFORMATION", "Insert Dishes_Ordering successfully")

        except EXCEPTION as e:
            print(e)
            mydb.rollback()
        mydb.close()


    def delete_Dishes_Ordering(self):
        global Id

        a = Id.get()
        try:
            sql = "DELETE FROM Dishes_Ordering WHERE Id = %s"
            val = (a,)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("INFORMATION", "Delete Dishes_Ordering successfully")

        except EXCEPTION as e:
            print(e)
            mydb.rollback()
        mydb.close()

    def update_Dishes_Ordering(self):
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
            messagebox.showinfo("INFORMATION", "Update Dishes_Ordering successfully")

        except EXCEPTION as e:
            print(e)
            mydb.rollback()
        mydb.close()

    def dis_customer(self):

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

    def Menu(self):

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

    def Exit(self):

        exit_program = messagebox.askyesno(
            title='Restaurant Management System',
            message='Confirm if you want to exit program?')
        if exit_program > 0:
            INTERFACE.root.destroy()
        else:
            return None

    def Reset(self):
        reset_program = messagebox.askyesno(
            title='Restaurant Management System',
            message='Confirm if you want to reset program?')
        if reset_program > 0:
            INTERFACE.interface.txtIdCus.delete(0, END)
            INTERFACE.interface.txtFull_Name.delete(0, END)
            INTERFACE.interface.txtPhone.delete(0, END)
            INTERFACE.interface.txtNumber_people.delete(0, END)
            INTERFACE.interface.txtArrive_time.delete(0, END)

            INTERFACE.interface.txtDish_Name.delete(0, END)
            INTERFACE.interface.txtPrice.delete(0, END)
            INTERFACE.interface.txt_id.delete(0, END)

            buttons.txt_reference.delete(0, END)
            buttons.txt_Buri.delete(0, END)
            buttons.txt_Grilled_cod_fish.delete(0, END)
            buttons.txt_Herring_fish.delete(0, END)
            buttons.txt_karikari.delete(0, END)
            buttons.txt_Saba.delete(0, END)

            buttons.txt_Salmon.delete(0, END)
            buttons.txt_Snapper.delete(0, END)
            buttons.txt_Chankonabe.delete(0, END)
            buttons.txt_Cost.delete(0, END)
            buttons.txt_Total.delete(0, END)
            buttons.txt_Services.delete(0, END)
        else:
            return None

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


    def Ref(self):
        x=random.randint(12980, 50876)
        randomRef = str(x)
        self.order_nu.set(randomRef)

        dist_1= float(buttons.txt_Buri.get())
        dist_2= float(buttons.txt_Grilled_cod_fish.get())
        dist_3= float(buttons.txt_Herring_fish.get())
        dist_4= float(buttons.txt_karikari.get())
        dist_5= float(buttons.txt_Saba.get())
        dist_6= float(buttons.txt_Salmon.get())
        dist_7= float(buttons.txt_Snapper.get())
        dist_8= float(buttons.txt_Chankonabe.get())


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

        self.Services.set(Service)
        self.Cost.set(Totalcost)
        self.Total.set(TotalOveraLL)
SQL = sqll()
class buttons:
# ===================================== Display table ordering =====================================#

    lbl_reference = Label(INTERFACE.interface.rightframe1,
                      font=('aria', 16, 'bold italic'),
                      text="Order No.",
                      fg="orchid3",
                      bd=10,
                      anchor='w')
    lbl_reference.grid(row=0, column=1)


    txt_reference = Entry(INTERFACE.interface.rightframe1,
                      font=('ariel', 16, 'bold italic'),
                      textvariable=sqll.order_nu,
                      bd=6,
                      insertwidth=4,
                      bg="white",
                      justify='right')
    txt_reference.grid(row=0,column=2)


    lbl_Buri = Label(INTERFACE.interface.rightframe1,
                 font=('aria', 16, 'bold italic'),
                 text="Buri",
                 fg="green",
                 bd=10,
                 anchor='w')
    lbl_Buri.grid(row=1, column=0)


    txt_Buri = Entry(INTERFACE.interface.rightframe1,
                 font=('ariel', 16, 'bold italic'),
                 textvariable=sqll.Buri,
                 bd=6,
                 insertwidth=4,
                 bg="white",
                 justify='right',
                 state=NORMAL)
    txt_Buri.grid(row=1, column=1)


    lbl_Grilled_cod_fish = Label(INTERFACE.interface.rightframe1,
                             font=('aria', 16, 'bold italic'),
                             text="Grilled cod fish ",
                             fg="green",
                             bd=10,
                             anchor='w')
    lbl_Grilled_cod_fish.grid(row=2, column=0)


    txt_Grilled_cod_fish = Entry(INTERFACE.interface.rightframe1,
                             font=('ariel', 16, 'bold italic'),
                             textvariable = sqll.Grilled_cod_fish,
                             bd=6,
                             insertwidth=4,
                             bg="white",
                             justify='right')
    txt_Grilled_cod_fish.grid(row=2, column=1)


    lbl_Herring_fish = Label(INTERFACE.interface.rightframe1,
                         font=('aria', 16, 'bold italic'),
                         text="Herring fish",
                         fg="green",
                         bd=10,
                         anchor='w')
    lbl_Herring_fish.grid(row=3, column=0)


    txt_Herring_fish = Entry(INTERFACE.interface.rightframe1,
                         font=('ariel', 16, 'bold italic'),
                         textvariable=sqll.Herring_fish,
                         bd=6,
                         insertwidth=4,
                         bg="white",
                         justify='right')
    txt_Herring_fish.grid(row=3, column=1)


    lbl_karikari = Label(INTERFACE.interface.rightframe1,
                     font=('aria', 16, 'bold italic'),
                     text="Karikari",
                     fg="green",
                     bd=10,
                     anchor='w')
    lbl_karikari.grid(row=4, column=0)


    txt_karikari = Entry(INTERFACE.interface.rightframe1,
                     font=('ariel', 16, 'bold italic'),
                     textvariable=sqll.karikari,
                     bd=6,
                     insertwidth=4,
                     bg="white",
                     justify='right')
    txt_karikari.grid(row=4, column=1)


    lbl_Saba = Label(INTERFACE.interface.rightframe1,
                 font=('aria', 16, 'bold italic'),
                 text="Saba",
                 fg="green",
                 bd=10,
                 anchor='w')
    lbl_Saba.grid(row=1, column=2)


    txt_Saba = Entry(INTERFACE.interface.rightframe1,
                 font=('ariel', 16, 'bold italic'),
                 textvariable=sqll.Saba,
                 bd=6,
                 insertwidth=4,
                 bg="white",
                 justify='right')
    txt_Saba.grid(row=1, column=3)


    lbl_Salmon = Label(INTERFACE.interface.rightframe1,
                   font=('aria', 16, 'bold italic'),
                   text="Salmon",
                   fg="green",
                   bd=10,
                   anchor='w')
    lbl_Salmon.grid(row=2, column=2)


    txt_Salmon = Entry(INTERFACE.interface.rightframe1,
                   font=('ariel', 16, 'bold italic'),
                   textvariable=sqll.Salmon,
                   bd=6,
                   insertwidth=4,
                   bg="white",
                   justify='right')
    txt_Salmon.grid(row=2, column=3)


    lbl_Snapper = Label(INTERFACE.interface.rightframe1,
                    font=('aria', 16, 'bold italic'),
                    text="Snapper",
                    fg="green",
                    bd=10,
                    anchor='w')
    lbl_Snapper.grid(row=3, column=2)


    txt_Snapper = Entry(INTERFACE.interface.rightframe1,
                    font=('ariel', 16,'bold italic'),
                    textvariable=sqll.Snapper,
                    bd=6,
                    insertwidth=4,
                    bg="white",
                    justify='right')
    txt_Snapper.grid(row=3, column=3)


    lbl_Chankonabe = Label(INTERFACE.interface.rightframe1,
                       font=('aria',16, 'bold italic' ),
                       text="Chankonabe",
                       fg="green",
                       bd=10,
                       anchor='w')
    lbl_Chankonabe.grid(row=4,column=2)


    txt_Chankonabe = Entry(INTERFACE.interface.rightframe1,
                       font=('ariel', 16, 'bold italic'),
                       textvariable=sqll.Chankonabe,
                       bd=6,
                       insertwidth=4,
                       bg="white",
                       justify='right')
    txt_Chankonabe.grid(row=4, column=3)

# ===================================== Calculate cost =====================================#

    lbl_Cost = Label(INTERFACE.interface.rightframe2,
                 font=('aria', 16, 'bold italic'),
                 text="Cost",
                 fg="orchid3",
                 bd=10,
                 anchor='w')
    lbl_Cost.grid(row=0, column=1)


    txt_Cost = Entry(INTERFACE.interface.rightframe2,
                 font=('ariel', 16, 'bold italic'),
                 textvariable=sqll.Cost,
                 bd=6,
                 insertwidth=4,
                 bg="white",
                 justify='right')
    txt_Cost.grid(row=0, column=2)


    lbl_Services = Label(INTERFACE.interface.rightframe2,
                     font=('aria', 16, 'bold italic'),
                     text="Services",
                     fg="orchid3",
                     bd=10,
                     anchor='w')
    lbl_Services.grid(row=1, column=1)


    txt_Services = Entry(INTERFACE.interface.rightframe2,
                     font=('ariel', 16, 'bold italic'),
                     textvariable=sqll.Services,
                     bd=6,
                     insertwidth=4,
                     bg="white",
                     justify='right')
    txt_Services.grid(row=1, column=2)


    lbl_Total = Label(INTERFACE.interface.rightframe2,
                  font=('aria', 16, 'bold italic'),
                  text="Total",
                  fg="red",
                  bd=10,
                  anchor='w')
    lbl_Total.grid(row=2, column=1)


    txt_Total = Entry(INTERFACE.interface.rightframe2,
                  font=('ariel', 16, 'bold italic'),
                  textvariable=sqll.Total,
                  bd=6,
                  insertwidth=4,
                  bg="white",
                  justify='right')
    txt_Total.grid(row=2, column=2)

# ===================================== Set logo_left for restaurant =====================================#

    load_banner= Image.open("./images/banner.jpg")
    render_banner = ImageTk.PhotoImage(load_banner)
    img_banner = Label(INTERFACE.interface.bottomFrame, image=render_banner, anchor=NW)
    img_banner.place(x=15, y=400)
# ===================================== List button option for user chooses =====================================#

    btnAdd = Button(INTERFACE.interface.bottomFrame,
                    bd=4,
                    font=('arial', 10, 'bold'),
                    width=15,
                    height=1,
                    text='Add Customer',
                    command=SQL.addCUS)
    btnAdd.grid(row=0, column=1, padx=4, pady=1)

    btndelete = Button(INTERFACE.interface.bottomFrame,
                       bd=4,
                       font=('arial', 10, 'bold'),
                       width=15,
                       height=1,
                       text='Delete Customer',
                       command=SQL.deleteCUS)
    btndelete.grid(row=0, column=2, padx=4, pady=1)

    btnUpdateCUS = Button(INTERFACE.interface.bottomFrame,
                          bd=4,
                          font=('arial', 10, 'bold'),
                          width=15,
                          height=1,
                          text='Update Customer',
                          command=SQL.updateCUS)
    btnUpdateCUS.grid(row=0, column=3, padx=4, pady=1)

    btnDisCus = Button(INTERFACE.interface.bottomFrame,
                       bd=4,
                       font=('arial', 10, 'bold'),
                       width=15,
                       height=1,
                       text='Display Customer',
                       command=SQL.dis_customer)
    btnDisCus.grid(row=0, column=4, padx=4, pady=1)

    btnAddDish = Button(INTERFACE.interface.bottomFrame,
                        bd=4,
                        font=('arial', 10, 'bold'),
                        width=15,
                        height=1,
                        text='Add Dish',
                        command=SQL.addPRODUCT)
    btnAddDish.grid(row=1, column=1, padx=4, pady=1)

    btndeleteproduct = Button(INTERFACE.interface.bottomFrame,
                              bd=4,
                              font=('arial', 10, 'bold'),
                              width=15,
                              height=1,
                              text='Delete Dish',
                              command=SQL.deletePRODUCT)
    btndeleteproduct.grid(row=1, column=2, padx=4, pady=1)

    btnUpdate_dish = Button(INTERFACE.interface.bottomFrame,
                            bd=4,
                            font=('arial', 10, 'bold'),
                            width=15,
                            height=1,
                            text='Update Dishes',
                            command=SQL.updatePRODUCT)
    btnUpdate_dish.grid(row=1, column=3, padx=4, pady=1)

    btnMenu = Button(INTERFACE.interface.bottomFrame,
                     bd=4,
                     font=('arial', 10, 'bold'),
                     width=15,
                     height=1,
                     text='Menu',
                     command=SQL.Menu)
    btnMenu.grid(row=1, column=4, padx=4, pady=1)

    btnTotal = Button(INTERFACE.interface.bottomFrame,
                      bd=4,
                      font=('arial', 10, 'bold'),
                      width=15,
                      height=1,
                      text='Total',
                      command=SQL.Ref)
    btnTotal.grid(row=2, column=1, padx=4, pady=1)

    btnReset = Button(INTERFACE.interface.bottomFrame,
                      bd=4,
                      font=('arial', 10, 'bold'),
                      width=15,
                      height=1,
                      text='Reset',
                      command=SQL.Reset)
    btnReset.grid(row=2, column=2, padx=4, pady=1)

    btnExit = Button(INTERFACE.interface.bottomFrame,
                     bd=4, font=('arial', 10, 'bold'),
                     width=15,
                     height=1,
                     text='Exit',
                     command=SQL.Exit)
    btnExit.grid(row=2, column=3, padx=4, pady=1)

