from datetime import *
import mysql.connector as my
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import time
from fpdf import FPDF

def connect():
    con=my.connect(host="localhost",user="root",password="7140",database="profiles")
    return con
class Customer:
    def __init__(self,logu,logpass):
        self.logu=logu
        self.logpass=logpass
        self.cust=Tk()
        self.cust.title("Movie selection")
        self.cust.config(background="light blue")
        self.cust.geometry("550x480")
        self.cust.resizable(0,100)
        try:
            self.con=connect()
            self.cur=self.con.cursor(buffered=True)
            self.cur.execute("SELECT * FROM movies")
            i=0
            label1=Label(self.cust,text="Movie",font='Verdana 10 bold',bg="light blue")
            label1.place(x=50,y=20)
            label2=Label(self.cust,text="Date",font='Verdana 10 bold',bg="light blue")
            label2.place(x=150,y=20)
            label1=Label(self.cust,text="Time",font='Verdana 10 bold',bg="light blue")
            label1.place(x=250,y=20)
            for movie in self.cur:
                for j in range(3):
                    e = Label(self.cust, text=movie[j], fg='red',font='Verdana 10 bold',bg="light blue") 
                    e.grid(row=i, column=j)
                    e.place(x=(j)*100+50,y=(i+1)*50)
                book=Button(self.cust, text = "book" ,font='Verdana 10 bold', 
                           command=lambda m=movie[0],d=movie[1],t=movie[2] :self.bookmovie(moviename=m,moviedate=d,movietime=t))
                book.place(x=400,y=(i+1)*50)      
                i+=1
        except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = self.cust)
        self.cust.mainloop()
    def bookmovie(self,moviename,moviedate,movietime):
        def action(val):
            try:
                self.cur.execute("Select * FROM movies where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                ans=self.cur.fetchone()

                if val==1:
                    if (ans[3]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 1a='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("1A")
                            movie.destroy()
                elif  val==2:
                    if (ans[4]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 1b='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("1B")
                            movie.destroy()
                elif  val==3:
                    if (ans[5]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 1c='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)  
                            ticket("1C") 
                            movie.destroy() 
                elif  val==4:
                    if (ans[6]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 2a='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("2A")
                            movie.destroy()
                elif  val==5:
                    if (ans[7]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 2b='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("2B")
                            movie.destroy()
                elif  val==6:
                    if (ans[8]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 2c='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("2C")
                            movie.destroy()
                if val==7:
                    if (ans[9]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                       
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 3a='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("3A")
                            movie.destroy()
                elif  val==8:
                    if (ans[10]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 3b='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("3B")
                            movie.destroy()
                elif  val==9:
                    if (ans[11]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 3c='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("3C")
                            movie.destroy()
                elif  val==10:
                    if (ans[12]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 4a='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("4A")
                            movie.destroy()
                elif  val==11:
                    if (ans[13]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 4b='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("4B")
                            movie.destroy()
                elif  val==12:
                    if (ans[14]==1):
                        messagebox.showerror("Error" , "Seat is already booked", parent = movie)
                    else:
                        
                        my_var=messagebox.askyesnocancel("Confirm","Want to book this ticket?",icon='warning',default='yes',parent=movie)
                        if my_var:
                            self.cur.execute("UPDATE movies SET 4c='1' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                            self.con.commit()
                            messagebox.showinfo("Success" , "Booking Successfully" , parent = movie)
                            ticket("4C")
                            movie.destroy()
                
            except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = movie)    
                    
        
        movie=Tk()
        movie.title("Ticket")
        movie.config(background="light blue")
        movie.geometry("450x360")
        movie.resizable(0,0)        
        
        self.cur.execute("Select * FROM movies where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
        ans=self.cur.fetchone()
        
        
        if (ans[3]==1):
            color="red"
        else:
            color="green"
        seat1a=Button(movie,text="1a", bg=color,command=lambda k=1 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat1a.place(x=100,y=50)
        if (ans[4]==1):
            color="red"
        else:
            color="green"
        seat1b=Button(movie,text="1b", bg=color,command=lambda k=2 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat1b.place(x=200,y=50)
        if (ans[5]==1):
            color="red"
        else:
            color="green"
        seat1c=Button(movie,text="1c", bg=color,command=lambda k=3 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat1c.place(x=300,y=50)
        
        if (ans[6]==1):
            color="red"
        else:
            color="green"
        seat2a=Button(movie,text="2a", bg=color,command=lambda k=4 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat2a.place(x=100,y=120)
        if (ans[7]==1):
            color="red"
        else:
            color="green"
        seat2b=Button(movie,text="2b", bg=color,command=lambda k=5 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat2b.place(x=200,y=120)
        if (ans[8]==1):
            color="red"
        else:
            color="green"
        seat2c=Button(movie,text="2c", bg=color,command=lambda k=6 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat2c.place(x=300,y=120)
        
        if (ans[9]==1):
            color="red"
        else:
            color="green"
        seat3a=Button(movie,text="3a", bg=color,command=lambda k=7 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat3a.place(x=100,y=190)
        if (ans[10]==1):
            color="red"
        else:
            color="green"
        seat3b=Button(movie,text="3b", bg=color,command=lambda k=8 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat3b.place(x=200,y=190)
        if (ans[11]==1):
            color="red"
        else:
            color="green"
        seat3c=Button(movie,text="3c", bg=color,command=lambda k=9 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat3c.place(x=300,y=190)
        if (ans[12]==1):
            color="red"
        else:
            color="green"
        seat4a=Button(movie,text="4a", bg=color,command=lambda k=10 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat4a.place(x=100,y=260)
        if (ans[13]==1):
            color="red"
        else:
            color="green"
        seat4b=Button(movie,text="4b", bg=color,command=lambda k=11 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat4b.place(x=200,y=260)
        if (ans[14]==1):
            color="red"
        else:
            color="green"
        seat4c=Button(movie,text="4c", bg=color,command=lambda k=12 :action(val=k),width=5,height=3,font='verdana 8 bold')
        seat4c.place(x=300,y=260)
        
        
        def ticket(seat):
            try:
                concust=connect()
                curcust=concust.cursor()
                curcust.execute("SELECT phone FROM customers WHERE username='"+self.logu+"' AND password='"+self.logpass+"'")
                phone=curcust.fetchone()
                
                messagebox.showinfo("Success" , "Please select where you want to download your ticket pdf" , parent = movie)
                file=asksaveasfilename(defaultextension=".pdf",filetypes=[("Text Documents","*.pdf"),("All Files","*.*")])
                
                
                base=open("ticket.txt","w")
                base.write("\tTicket\n")
                base.write("Username :"+self.logu+"\n"+"Phone no. :"+phone[0]+"\n")
                base.write("Movie:"+moviename+"\n"+"Date :"+str(moviedate)+"\n"+"Time (24 hour format) :"+str(movietime)+"\n")
                base.write("Your Seat:"+seat+"\n")
                base.write("Thank you :)")
                base.close()
                
                pdf=FPDF()
                pdf.add_page()
                pdf.set_font("Arial",size=15)
                r=open("ticket.txt","r")
                for x in r:
                    pdf.cell(200,10,txt=x,ln=1)
                
                pdf.output(file)
            except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = movie)    
        movie.mainloop()
            