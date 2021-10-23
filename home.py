import mysql.connector as my
from tkinter import *
from tkinter import messagebox
import time
from Admin import emploginfunc
from customer import Customer
def clear():
    lusername.delete(0,END)
    password.delete(0,END)

def close():
    win.destroy()

def connect():
    con=my.connect(host="localhost",user="root",password="7140",database="profiles")
    return con


def loginfunc():
    if lusername.get()=="" or password.get()=="":
        messagebox.showerror("Error","Fields are empty",parent=win)
    else:
        try:
            con=connect()
            cur=con.cursor()
            logu=lusername.get()
            logpass=password.get()
            cur.execute("select * from customers where username=%s and password=%s",(lusername.get(),password.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)
            else:
                messagebox.showinfo("Success" , "Successfully Login" , parent = win)
                close()
                c=Customer(logu,logpass)
            con.close()
        except Exception as ez:
            messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = win)
            

def signupfunc():
    def action():
        if username.get()=="" or email.get()=="" or phone.get()=="" or passw.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
        elif passw.get()!=rpassw.get():
            messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
        else:
            try:
                con=connect()
                cur=con.cursor()
                cur.execute("select * from customers where username='"+username.get()+"'")
                row=cur.fetchone()
                print("gg")
                x=1
                if row!=None:
                    messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
                else:
                    cur.execute("insert into customers(username,email,phone,password) values(%s,%s,%s,%s)",
                                (
                                    username.get(),email.get(),phone.get(),passw.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success" , "Registration Successfull" , parent = winsignup)
                    clear()
                    switch()
            except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = winsignup)    
    def switch():
        winsignup.destroy()
    
    def clear():
        username.delete(0,END)
        email.delete(0,END)
        phone.delete(0,END)
        passw.delete(0,END)
        rpassw.delete(0,END)
    
    winsignup=Tk()
    winsignup.title("signup")
    winsignup.config(background="light blue")
    winsignup.geometry("640x480")
    winsignup.resizable(0,0)

    username=StringVar()
    ename=Label(winsignup,text="Enter Username:",font=("Arial",15),fg="black",bg="light blue")
    ename.place(x=30,y=30)
    username=Entry(winsignup,textvariable=username,font=("Arial",12))
    username.place(x=200,y=30,height=30,width=200)

    eemail=Label(winsignup,text="Enter Email ID:",font=("Arial",15),fg="black",bg="light blue")
    eemail.place(x=30,y=90)
    email=Entry(winsignup,textvariable=StringVar(),font=("Arial",12))
    email.place(x=200,y=90,height=30,width=200)

    ephone=Label(winsignup,text="Contact number :",font=("Arial",15),fg="black",bg="light blue")
    ephone.place(x=30,y=150)
    phone=Entry(winsignup,textvariable="",font=("Arial",12))
    phone.place(x=200,y=150,height=30,width=200)

    epw=Label(winsignup,text="Enter password :",font=("Arial",15),fg="black",bg="light blue")
    epw.place(x=30,y=210)
    passw=Entry(winsignup,textvariable=StringVar(),font=("Arial",12),show="*")
    passw.place(x=200,y=210,height=30,width=200)
    erpw=Label(winsignup,text="Re-enter password :",font=("Arial",15),fg="black",bg="light blue")
    erpw.place(x=30,y=270)
    rpassw=Entry(winsignup,textvariable=StringVar(),font=("Arial",12),show="*")
    rpassw.place(x=240,y=270,height=30,width=200)
    
    signupp=Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action,width=8,height=2)
    signupp.place(x=160,y=350)
    
    btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear, width=8,height=2)
    btn_login.place(x=300, y=350)
    
    golog=PhotoImage(file=r"login.png").subsample(3,3)
    sign_up_btn = Button(winsignup , text="Login" ,font='Verdana 10 bold', command = switch, width=8,height=2 )
    sign_up_btn.place(x=440 , y =350)
    
    
    winsignup.mainloop()
    
con=connect()
mycur=con.cursor()
mycur.execute("CREATE TABLE if not exists customers (username VARCHAR(255),email VARCHAR(255),phone VARCHAR(255), password VARCHAR(255))")
mycur.execute("CREATE TABLE if not exists Employee (empid VARCHAR(255), password VARCHAR(255))")
mycur.execute("CREATE TABLE if not exists Movies (movie VARCHAR(255), date DATE ,time TIME, 1a INT, 1b INT, 1c INT, 2a INT, 2b INT, 2c INT, 3a INT, 3b INT, 3c INT, 4a INT, 4b INT, 4c INT )")

win=Tk()
win.title("Movie Genie")
win.geometry("500x380")
win.config(bg="light blue")
win.resizable(0,0)

# bg=PhotoImage(file=r"backg.png")
# blabel=Label(win,image=bg)
# blabel.place(x=0,y=0)
# blabel.pack(fill=BOTH)

eusname=Label(win,text="Enter Username:",font=("Arial",15),fg="black",bg="light blue")
eusname.place(x=30,y=30)
lusername=Entry(win,textvariable=StringVar(),font=("Arial",12))
lusername.place(x=200,y=30,height=30,width=200)
epw=Label(win,text="Enter password :",font=("Arial",15),fg="black",bg="light blue")
epw.place(x=30,y=100)
password=Entry(win,textvariable=StringVar(),font=("Arial",12),show="*")
password.place(x=200,y=100,height=30,width=200)


btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = loginfunc,width=8,height=2)
btn_login.place(x=160, y=150)

btn_login1 = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear, width=8,height=2)
btn_login1.place(x=300, y=150)
signupimage=PhotoImage(file=r"signup.png").subsample(10,11)
sign_up_btn = Button(win , text="Sign up" ,font='Verdana 8 bold', command = signupfunc,image=signupimage,compound=LEFT )
sign_up_btn.place(x=135 , y =250)
adminimage=PhotoImage(file=r"admin.png").subsample(7,6)
adminlog = Button(win , text="Staff login" ,font='Verdana 8 bold', command = emploginfunc,image=adminimage,compound=LEFT )
# adminlog = Button(win , text="Staff login" ,font='Verdana 8 bold', command = emploginfunc)
adminlog.place(x=300 , y =250)
# adminlog.pack(side=TOP)


win.mainloop()