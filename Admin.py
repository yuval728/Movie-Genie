import mysql.connector as my
from tkinter import *
from tkinter import messagebox
import time
import staffoper as so

def connect():
    con=my.connect(host="localhost",user="root",password="7140",database="profiles")
    return con

def emploginfunc():
    def switch():
        staff.destroy()
    def action():
       if lempid.get()=="" or password.get()=="":
            messagebox.showerror("Error",parent=staff)
       else:
            try:
                con=connect()
                cur=con.cursor()
                cur.execute("select * from employee where empid=%s and password=%s",(lempid.get(),password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error" , "Invalid ID And Password", parent = staff)
                else:
                    messagebox.showinfo("Success" , "Successfully Login" , parent = staff)
                    
                    switch()
                    so.operation()
                    
                con.close()
            except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = staff)
    staff=Tk()
    staff.title("Staff")
    staff.config(background="light blue")
    staff.geometry("450x270")
    staff.resizable(0,0)
    eusname=Label(staff,text="Enter EMP ID:",font=("Arial",15),fg="black",bg="light blue")
    eusname.place(x=30,y=30)
    lempid=Entry(staff,textvariable=StringVar(),font=("Arial",12))
    lempid.place(x=200,y=30,height=30,width=200)
    epw=Label(staff,text="Enter password :",font=("Arial",15),fg="black",bg="light blue")
    epw.place(x=30,y=100)
    password=Entry(staff,textvariable=StringVar(),font=("Arial",12),show="*")
    password.place(x=200,y=100,height=30,width=200)
    logg=Button(staff, text = "Login" ,font='Verdana 8 bold', command = action,height=2,width=8)
    logg.place(x=180,y=160)
    back=Button(staff, text = "Customer \nLogin" ,font='Verdana 8 bold', command = switch,height=2,width=8)
    back.place(x=280,y=160)