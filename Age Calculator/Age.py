from tkinter import *
from datetime import date

root=Tk()   # Creating a window
root.title("Age Calculator")    # setting up title
root.configure(bg="#D5C6FF")    # setting up background color
root.geometry("400x300")    # Fixing the size of the window
new=Label(root,bg="#D5C6FF")  # Declaring a lable
new.grid(row=5,column=0,columnspan=3)

today=str(date.today())    # Getting current date using datetime module
list_today=today.split("-")  # Converting into a list
# Defining a function to calcutate age
def age(b_date,b_month,b_year):
    global today
    global new
    new.grid_forget()
    b_date=int(entry_date.get())
    b_month=int(entry_month.get())
    b_year=int(entry_year.get())
    c_date=int(list_today[2])
    c_month=int(list_today[1])
    c_year=int(list_today[0])
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(b_date>c_date):
        c_month=c_month-1
        c_date=c_date+month[b_month-1]
    if (b_month>c_month):
        c_year=c_year-1
        c_month=c_month+12
    resultd=str(c_date-b_date)
    resultm=str(c_month-b_month)
    resulty=str(c_year-b_year)
    new=Label(root,text="Your Age: \n"+resulty+" Years "+resultm+" Months "+ resultd+" Days ",fg="#990099",bg="#D5C6FF",borderwidth=6)
    new.config(font=("Calibri Bold",15))
    new.grid(row=5,column=0,columnspan=3)

# Defining a function to clear the previous entries
def clean(entry_date,entry_month,entry_year):
    global new
    new.grid_forget()
    entry_date.delete(0,END)
    entry_month.delete(0,END)
    entry_year.delete(0,END)

# Creating widgets such as labels,entry boxes and buttons and fixing its position onto window    
title_label=Label(root,text="AGE CALCULATOR",borderwidth=10,fg="#6600CC",bg="#D5C6FF")
title_label.config(font=("Broadway",29))
title_label.grid(row=0,column=0,columnspan=3)
label_date=Label(root,text="Date of Birth : ",borderwidth=4,fg="#990099",bg="#D5C6FF")
label_date.config(font=("Calibri Bold",15))
label_date.grid(row=1,column=0)
label_month=Label(root,text="Month of Birth : ",borderwidth=5,fg="#990099",bg="#D5C6FF")
label_month.config(font=("Calibri Bold",15))
label_month.grid(row=2,column=0)
label_year=Label(root,text="Year of Birth : ",borderwidth=9,fg="#990099",bg="#D5C6FF")
label_year.config(font=("Calibri Bold",15))
label_year.grid(row=3,column=0)

entry_date=Entry(root,width=20,borderwidth=3)
entry_month=Entry(root,width=20,borderwidth=3)
entry_year=Entry(root,width=20,borderwidth=3)

entry_date.grid(row=1,column=2)
entry_month.grid(row=2,column=2)
entry_year.grid(row=3,column=2)

# Getting the value in the entry boxes
b_date=entry_date.get()
b_month=entry_month.get()
b_year=entry_year.get()

# Calling age function in button widget
submit=Button(root,text="Calculate Age!",width=10,anchor=CENTER,command=lambda:age(b_date,b_month,b_year),bg="#6600CC",fg="#D5C6FF",borderwidth=5)
submit.grid(row=4,column=0)

# Calling  clean function in button widget
clear=Button(root,text="Clear",width=10,command=lambda:clean(entry_date,entry_month,entry_year),bg="#6600CC",fg="#D5C6FF",borderwidth=5)
clear.grid(row=4,column=2)
root.mainloop()