from tkinter import* 
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk,Image 
import random
import time
import sqlite3
from student import Student


root = Tk()
# Set screen initial
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")



Tops = Frame(root,bg="green2",width = 1600,height=50,relief=RAISED)
Tops.pack(side=TOP)

# set logo_left for restaurant
load= Image.open("./images/logo.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render, anchor=NW)
img.place(x=50, y=17)

# set logo_right for restaurant
load_logo_right= Image.open("./images/banner.jpg")
render_logo_right = ImageTk.PhotoImage(load_logo_right)
img_logo_right = Label(root, image=render_logo_right, anchor=NE)
img_logo_right.place(x=1060, y=20)

# ----------------- create block left have 70% -----------------#
block_left = Frame(root,width = 900,height=700,relief=SUNKEN)
block_left.pack(side=LEFT)

# ----------------- create block right have 30% -----------------#
block_right = Frame(root ,width = 400,height=700,relief=SUNKEN)
block_right.pack(side=RIGHT)

# ----------------- set current time -----------------#
localtime=time.asctime(time.localtime(time.time()))


#-----------------INFO TOP------------
lbl_info = Label(Tops, font=( 'Helvetica' ,30, 'bold' ),text="Restaurant Management System",bg="slate gray",fg="white",bd=10,anchor='center')
lbl_info.grid(row=0,column=0)
lbl_info = Label(Tops, font=( "Times", 24, "bold italic" ),text=localtime, bg="gainsboro",fg="black",anchor='center')
lbl_info.grid(row=1,column=0)


# ================ Block_right ================ #

#---------------Calculator------------------
text_Input=StringVar()
operator =""

txt_display = Entry(block_right,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txt_display.grid(columnspan=4)

# function to get value in user
def  bottom_click(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

# function to clear all in screen calculator
def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

# function to calculate equation
def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

# buttom in calculator
#----------------------------------------row 1----------------------------------------#
btn7=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="light blue",relief=RIDGE, command=lambda: bottom_click(7))
btn7.grid(row=2,column=0)

btn8=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="8",bg="light blue",relief=RIDGE, command=lambda: bottom_click(8) )
btn8.grid(row=2,column=1)

btn9=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="9",bg="light blue",relief=RIDGE, command=lambda: bottom_click(9) )
btn9.grid(row=2,column=2)

Addition=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="+",bg="light blue",relief=RIDGE, command=lambda: bottom_click("+") )
Addition.grid(row=2,column=3)
#----------------------------------------row 2----------------------------------------#
btn4=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="4",bg="light blue",relief=RIDGE, command=lambda: bottom_click(4) )
btn4.grid(row=3,column=0)

btn5=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="5",bg="light blue",relief=RIDGE, command=lambda: bottom_click(5) )
btn5.grid(row=3,column=1)

btn6=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="6",bg="light blue",relief=RIDGE, command=lambda: bottom_click(6) )
btn6.grid(row=3,column=2)

Substraction=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="-",bg="light blue",relief=RIDGE, command=lambda: bottom_click("-") )
Substraction.grid(row=3,column=3)
#----------------------------------------row 3----------------------------------------#
btn1=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="1",bg="light blue",relief=RIDGE, command=lambda: bottom_click(1) )
btn1.grid(row=4,column=0)

btn2=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="2",bg="light blue",relief=RIDGE, command=lambda: bottom_click(2) )
btn2.grid(row=4,column=1)

btn3=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="3",bg="light blue",relief=RIDGE, command=lambda: bottom_click(3) )
btn3.grid(row=4,column=2)

multiply=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 21 ,'bold'),text="*",bg="light blue",relief=RIDGE, command=lambda: bottom_click("*") )
multiply.grid(row=4,column=3)
#----------------------------------------row 4----------------------------------------#
btn0=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 20 ,'bold'),text="0",bg="light blue",relief=RIDGE, command=lambda: bottom_click(0) )
btn0.grid(row=5,column=0)

btn_C=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 19 ,'bold'),text="C",bg="light blue",relief=RIDGE, command=clrdisplay)
btn_C.grid(row=5,column=1)

Decimal=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 21 ,'bold'),text=".",bg="light blue",relief=RIDGE, command=lambda: bottom_click(".") )
Decimal.grid(row=5,column=2)

Division=Button(block_right,padx=16,pady=16,bd=3, fg="black", font=('ariel', 21 ,'bold'),text="/",bg="light blue",relief=RIDGE, command=lambda: bottom_click("/") )
Division.grid(row=5,column=3)

btn_equal=Button(block_right,padx=16,pady=16,bd=3,width = 16, fg="black", font=('ariel', 20 ,'bold'),text="=",bg="light blue",relief=RIDGE,command=eqals)
btn_equal.grid(columnspan=4)


# ================ Block_left(menu) ================ #
def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    order_nu.set(randomRef)

    dist_1 =float(Buri.get())
    dist_2= float(Grilled_cod_fish.get())
    dist_3= float(Herring_fish.get())
    dist_4= float(Octopus.get())
    dist_5= float(Saba.get())
    dist_6= float(Salmon.get())
    dist_7= float(Snapper.get())
    dist_8= float(Bo_bia.get())

    Buri_price = dist_1*50
    Grilled_cod_fish_price = dist_2*60
    Herring_fish_price = dist_3*250
    Octopus_price = dist_4*50
    Saba_price = dist_5*75
    Salmon_price = dist_6*45
    Snapper_price = dist_7*85
    Bo_bia_price = dist_8*15 


    Totalcost=(Buri_price +  Grilled_cod_fish_price + Herring_fish_price + Octopus_price  + Saba_price + Salmon_price + Snapper_price + Bo_bia_price)
    Service = ((Buri_price +  Grilled_cod_fish_price + Herring_fish_price + Octopus_price  + Saba_price + Salmon_price + Snapper_price + Bo_bia_price)*0.1)
    TotalOveraLL = str(Totalcost + Service),"$"

    Services.set(Service)
    Cost.set(Totalcost)
    Total.set(TotalOveraLL)

order_nu = StringVar()
Buri = StringVar()
Grilled_cod_fish = StringVar()
Herring_fish = StringVar()
Octopus = StringVar()
Saba = StringVar()
Salmon = StringVar()
Snapper = StringVar()
Bo_bia = StringVar()
Cost = StringVar()
Services = StringVar()
Total = StringVar()

lbl_reference = Label(block_left, font=( 'aria' ,16, 'bold italic' ),text="Order No.",fg="orchid3",bd=10,anchor='w')
lbl_reference.grid(row=0,column=0)
txt_reference = Entry(block_left, font=('ariel' ,16,'bold italic'), textvariable=order_nu, bd=6, insertwidth=4, bg="white", justify='right')
txt_reference.grid(row=0,column=1)

lbl_Buri = Label(block_left, font=('aria' , 16, 'bold italic'), text="Buri", fg="green", bd=10, anchor='w')
lbl_Buri.grid(row=1, column=0)
txt_Buri = Entry(block_left, font=('ariel' , 16, 'bold italic'), textvariable=Buri, bd=6, insertwidth=4, bg="white", justify='right')
txt_Buri.grid(row=1, column=1)

lbl_Grilled_cod_fish = Label(block_left, font=('aria' , 16, 'bold italic'), text="Grilled cod fish ", fg="green", bd=10, anchor='w')
lbl_Grilled_cod_fish.grid(row=2, column=0)
txt_Grilled_cod_fish = Entry(block_left, font=('ariel' , 16, 'bold italic'), textvariable=Grilled_cod_fish, bd=6, insertwidth=4, bg="white", justify='right')
txt_Grilled_cod_fish.grid(row=2, column=1)

lbl_Herring_fish = Label(block_left, font=('aria' , 16, 'bold italic'), text="Herring fish", fg="green", bd=10, anchor='w')
lbl_Herring_fish.grid(row=3, column=0)
txt_Herring_fish = Entry(block_left, font=('ariel' , 16, 'bold italic'), textvariable=Herring_fish, bd=6, insertwidth=4, bg="white", justify='right')
txt_Herring_fish.grid(row=3, column=1)

lbl_karikari = Label(block_left, font=('aria' , 16, 'bold italic'), text="Octopus", fg="green", bd=10, anchor='w')
lbl_karikari.grid(row=4, column=0)
txt_karikari = Entry(block_left, font=('ariel' , 16, 'bold italic'), textvariable=Octopus, bd=6, insertwidth=4, bg="white", justify='right')
txt_karikari.grid(row=4, column=1)

lbl_Saba = Label(block_left, font=('aria' , 16, 'bold italic'), text="Saba", fg="green", bd=10, anchor='w')
lbl_Saba.grid(row=5, column=0)
txt_Saba = Entry(block_left, font=('ariel' , 16, 'bold italic'), textvariable=Saba, bd=6, insertwidth=4, bg="white", justify='right')
txt_Saba.grid(row=5, column=1)

lbl_Salmon = Label(block_left, font=('aria' , 16, 'bold italic'), text="Salmon", fg="green", bd=10, anchor='w')
lbl_Salmon.grid(row=0, column=2)
txt_Salmon = Entry(block_left, font=('ariel' , 16, 'bold italic'), textvariable=Salmon, bd=6, insertwidth=4, bg="white", justify='right')
txt_Salmon.grid(row=0, column=3)

lbl_Snapper = Label(block_left, font=( 'aria' ,16, 'bold italic' ),text="Snapper",fg="green",bd=10,anchor='w')
lbl_Snapper.grid(row=1,column=2)
txt_Snapper = Entry(block_left,font=('ariel' ,16,'bold italic'), textvariable=Snapper , bd=6,insertwidth=4,bg="white" ,justify='right')
txt_Snapper.grid(row=1,column=3)

lbl_Bo_bia = Label(block_left, font=( 'aria' ,16, 'bold italic' ),text="Bo_bia",fg="green",bd=10,anchor='w')
lbl_Bo_bia.grid(row=2,column=2)
txt_Bo_bia = Entry(block_left,font=('ariel' ,16,'bold italic'), textvariable=Bo_bia , bd=6,insertwidth=4,bg="white" ,justify='right')
txt_Bo_bia.grid(row=2,column=3)

lbl_Cost = Label(block_left, font=( 'aria' ,16, 'bold italic' ),text="Cost",fg="orchid3",bd=10,anchor='w')
lbl_Cost.grid(row=3,column=2)
txt_Cost = Entry(block_left,font=('ariel' ,16,'bold italic'), textvariable=Cost , bd=6,insertwidth=4,bg="white" ,justify='right')
txt_Cost.grid(row=3,column=3)

lbl_Services = Label(block_left, font=( 'aria' ,16, 'bold italic' ),text="Services",fg="orchid3",bd=10,anchor='w')
lbl_Services.grid(row=4,column=2)
txt_Services = Entry(block_left,font=('ariel' ,16,'bold italic'), textvariable=Services , bd=6,insertwidth=4,bg="white" ,justify='right')
txt_Services.grid(row=4,column=3)

lbl_Total = Label(block_left, font=( 'aria' ,16, 'bold italic' ),text="Total",fg="red",bd=10,anchor='w')
lbl_Total.grid(row=5,column=2)
txt_Total = Entry(block_left,font=('ariel' ,16,'bold italic'), textvariable=Total , bd=6,insertwidth=4,bg="white" ,justify='right')
txt_Total.grid(row=5,column=3)


# ================ Buttom_bottom ================ #
def exit():
    root.destroy()

def reset():
    order_nu.set("")
    Buri.set("")
    Grilled_cod_fish.set("")
    Herring_fish.set("")
    Octopus.set("")
    Saba.set("")
    Salmon.set("")
    Snapper.set("")
    Bo_bia.set("")
    Cost.set("")
    Services.set("")
    Total.set("")

lbl_Total = Label(block_left,text="----------TotalOverAll-----------",fg="red")
lbl_Total.grid(row=6,columnspan=3)

btnTotal=Button(block_left,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="blue",command=Ref)
btnTotal.grid(row=7, column=1)

btn_reset=Button(block_left,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="green",command=reset)
btn_reset.grid(row=7, column=2)

btn_exit=Button(block_left,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=exit)
btn_exit.grid(row=7, column=3)


def price():
    roo = tk.Tk()
    roo.geometry("500x300+0+0")
    roo.title("Price List")
    lbl_restaurant = Label(roo, font=('aria', 15, 'bold italic'), text="Products", bg="burlywood3", fg="black", bd=5)
    lbl_restaurant.grid(row=0, column=0)
    lbl_restaurant = Label(roo, font=('aria', 15,'bold'), text="_________(-.-)_________", fg="OliveDrab1")
    lbl_restaurant.grid(row=0, column=2)
    lbl_restaurant = Label(roo, font=('aria', 15, 'bold italic'),padx=15, text="Price",bg="burlywood3", fg="black", bd=5)
    lbl_restaurant.grid(row=0, column=4)

    lbl_dist = Label(roo, font=('aria', 15, 'bold italic'), text="Buri", fg="sky blue", anchor=W)
    lbl_dist.grid(row=1, column=0)
    lbl_dist = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", anchor=W)
    lbl_dist.grid(row=1, column=4)
    lbl_dist = Label(roo, font=('aria', 15, 'bold italic'), text="Grilled_cod_fish", fg="sky blue", anchor=W)
    lbl_dist.grid(row=2, column=0)
    lbl_dist = Label(roo, font=('aria', 15, 'bold'), text="60", fg="red", anchor=W)
    lbl_dist.grid(row=2, column=4)
    lbl_dist = Label(roo, font=('aria', 15, 'bold italic'), text="Herring_fish", fg="sky blue", anchor=W)
    lbl_dist.grid(row=3, column=0)
    lbl_dist = Label(roo, font=('aria', 15, 'bold'), text="250", fg="red", anchor=W)
    lbl_dist.grid(row=3, column=4)
    lbl_dist = Label(roo, font=('aria', 15, 'bold italic'), text="Octopus", fg="sky blue", anchor=W)
    lbl_dist.grid(row=4, column=0)
    lbl_dist = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", anchor=W)
    lbl_dist.grid(row=4, column=4)
    lbl_dist = Label(roo, font=('aria', 15, 'bold italic'), text="Saba", fg="sky blue", anchor=W)
    lbl_dist.grid(row=5, column=0)
    lbl_dist = Label(roo, font=('aria', 15, 'bold'), text="45", fg="red", anchor=W)
    lbl_dist.grid(row=5, column=4)
    lbl_dist = Label(roo, font=('aria', 15, 'bold italic'), text="Salmon", fg="sky blue", anchor=W)
    lbl_dist.grid(row=6, column=0)
    lbl_dist = Label(roo, font=('aria', 15, 'bold'), text="75", fg="red", anchor=W)
    lbl_dist.grid(row=6, column=4)
    lbl_dist = Label(roo, font=('aria', 15, 'bold italic'), text="Snapper", fg="sky blue", anchor=W)
    lbl_dist.grid(row=7, column=0)
    lbl_dist = Label(roo, font=('aria', 15, 'bold'), text="85", fg="red", anchor=W)
    lbl_dist.grid(row=7, column=4)
    lbl_dist = Label(roo, font=('aria', 15, 'bold italic'), text="Bo_bia", fg="sky blue", anchor=W)
    lbl_dist.grid(row=8, column=0)
    lbl_dist = Label(roo, font=('aria', 15, 'bold'), text="15", fg="red", anchor=W)
    lbl_dist.grid(row=8, column=4)

    roo.mainloop()



btn_price=Button(block_left,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="green",command=price)
btn_price.grid(row=7, column=0)

def call_back():
    student_display = Student
    return student_display

btn_add_customer=Button(block_left,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Add Customer", bg="deep sky blue", command=call_back)
btn_add_customer.grid(row=9, column=1)

btn_add_dishes=Button(block_left,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Add Dishes", bg="deep sky blue",command=price)
btn_add_dishes.grid(row=9, column=2)


root.mainloop()

# syntax to use the Frame widget is given below. 
'''
1	bd	                It represents the border width.
2	bg	                The background color of the widget.
3	cursor	            The mouse pointer is changed to the cursor type set to different values like an arrow, dot, etc.
4	height	            The height of the frame.
5	highlightbackground	The color of the background color when it is under focus.
6	highlightcolor	    The text color when the widget is under focus.
7	highlightthickness	It specifies the thickness around the border when the widget is under the focus.
8	relief	            It specifies the type of the border. The default value if FLAT.
9	width	            It represents the width of the widget.
'''