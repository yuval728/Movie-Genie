from datetime import *
import mysql.connector as my
from tkinter import *
from tkinter import messagebox,ttk
import time

def connect():
    con=my.connect(host="localhost",user="root",password="7140",database="profiles")
    return con

class operation():
    def __init__(self):
        
        self.operate=Tk()
        self.operate.title("Operation")
        self.operate.config(background="light blue")
        self.operate.geometry("600x480")
        self.operate.resizable(False,True)
        
        try:
            self.con=connect()
            self.cur=self.con.cursor()
            self.cur.execute("SELECT * FROM movies")
            i=0
            label1=Label(self.operate,text="Movie",font='Verdana 10 bold',bg="light blue")
            label1.place(x=50,y=20)
            label2=Label(self.operate,text="Date",font='Verdana 10 bold',bg="light blue")
            label2.place(x=150,y=20)
            label1=Label(self.operate,text="Time",font='Verdana 10 bold',bg="light blue")
            label1.place(x=250,y=20)
            for movie in self.cur:
                for j in range(3):
                    e = Label(self.operate, text=movie[j], fg='red',font='Verdana 10 bold',bg="light blue") 
                    e.grid(row=i, column=j)
                    e.place(x=(j)*100+50,y=(i+1)*50)
                delet=Button(self.operate, text = "Delete" ,font='Verdana 10 bold', 
                           command=lambda m=movie[0],d=movie[1],t=movie[2] :self.deletemovie(moviename=m,moviedate=d,movietime=t))
                delet.place(x=450,y=(i+1)*50)   
                update=Button(self.operate, text = "Update" ,font='Verdana 10 bold', 
                           command=lambda m=movie[0],d=movie[1],t=movie[2] :self.updatemovie(moviename=m,moviedate=d,movietime=t))
                update.place(x=350,y=(i+1)*50)   
                i+=1
            # scroll=ttk.Scrollbar(self.operate,orient="vertical",command=label1.yview).pack(side=RIGHT,fill=Y)
            # label1['yscrollcommand']=scroll.set
        except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = self.operate)
                
        add=Button(self.operate, text = "Add movie" ,font='Verdana 10 bold', command=self.addmovie)
        add.place(x=380,y=10)
        
        
        # self.operate(yscrollcommand=scroll.set)
        self.operate.mainloop()    
    def addmovie(self):
        
        def action():
            if name.get()=="" or date.get()=="" or tim.get()=="":
                messagebox.showerror("Error",parent=movie)
            else:
                try:
                    mtime=time.strptime(tim.get(),'%H:%M:%S')
                    mdate=datetime.strptime(date.get(),'%Y-%m-%d').date()
                    self.cur.execute("insert into movies(movie,date,time) values(%s,%s,%s)",
                                (
                                    name.get(),date.get(),mtime
                                ))
                
                    self.con.commit()
                    self.con.close()
                    messagebox.showinfo("Success" , "Registration Successfull" , parent = movie)
                    movie.destroy()
                    self.operate.destroy()
                    op=operation()
                except Exception as ez:
                    messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = movie)
        movie=Tk()
        movie.title("Add")
        movie.config(background="light blue")
        movie.geometry("450x300")
        movie.resizable(0,0)
        
        aname=Label(movie,text="Enter Movie:",font=("Arial",15),fg="black",bg="light blue")
        aname.place(x=30,y=30)
        name=Entry(movie,textvariable=StringVar(),font=("Arial",12))
        name.place(x=150,y=30,height=30,width=200)
        adate=Label(movie,text="Enter Date:",font=("Arial",15),fg="black",bg="light blue")
        adate.place(x=30,y=90)
        afdate=Label(movie,text="(year-month-day)",font=("Arial",15),fg="black",bg="light blue")
        afdate.place(x=30,y=125)
        date=Entry(movie,textvariable=StringVar(),font=("Arial",12))
        date.place(x=150,y=90,height=30,width=200)
        # cal = Calendar(movie, selectmode = 'day',
        #        year = 2021, month = 10,
        #        day = 21)
        # cal.place(x=150,y=90)
        # timepick=AnalogPicker(movie)
        # timepick.place(x=300,y=90)
        # theme = AnalogThemes(timepick)
        # theme.setDracula()
        
        atime=Label(movie,text="Enter time:",font=("Arial",15),fg="black",bg="light blue")
        atime.place(x=30,y=170)
        afdate=Label(movie,text="(HH:MM:SS)",font=("Arial",15),fg="black",bg="light blue")
        afdate.place(x=30,y=195)
        tim=Entry(movie,textvariable=StringVar(),font=("Arial",12))
        tim.place(x=150,y=170,height=30,width=200)
        
        addm=Button(movie, text = "Add " ,font='Verdana 10 bold', command=action,width=8,height=1)
        addm.place(x=200,y=220)
        movie.mainloop()
    def deletemovie(self,moviename,moviedate,movietime):
        my_var=messagebox.askyesnocancel("Delete ?","Want to delete",icon='warning',default='no',parent=self.operate)
        if my_var:
            try:
                
                self.cur.execute("DELETE  FROM profiles.movies where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                self.con.commit()
                self.con.close()
                messagebox.showinfo("Success" , "Deleted Successfully" , parent = self.operate)
                self.operate.destroy()
                op=operation()
            except Exception as ez:
                messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent =self.operate)
    
    def updatemovie(self,moviename,moviedate,movietime):
        def action():
            if date.get()=="" or tim.get()=="":
                messagebox.showerror("Error",parent=movie)
            else:
                try:
                    mtime=time.strptime(tim.get(),'%H:%M:%S')
                    mdate=datetime.strptime(date.get(),'%Y-%m-%d').date()
                    self.cur.execute("UPDATE movies SET date='"+date.get()+"', time='"+tim.get()+"' where movie='"+str(moviename)+"'and date='"+str(moviedate)+"' and time='"+str(movietime)+"'")
                    self.con.commit()
                    self.con.close()
                    messagebox.showinfo("Success" , "update Successfull" , parent = movie)
                    movie.destroy()
                    self.operate.destroy()
                    op=operation()
                except Exception as ez:
                    messagebox.showerror("Error" , f"Error Due to : {str(ez)}", parent = movie)
        movie=Tk()
        movie.title("Update")
        movie.config(background="light blue")
        movie.geometry("450x250")
        movie.resizable(0,0)
        
        adate=Label(movie,text="Enter new Date:",font=("Arial",15),fg="black",bg="light blue")
        adate.place(x=30,y=90-30)
        afdate=Label(movie,text="(year-month-day)",font=("Arial",15),fg="black",bg="light blue")
        afdate.place(x=30,y=115-30)
        date=Entry(movie,textvariable=StringVar(),font=("Arial",12))
        date.place(x=200,y=90-30,height=30,width=200)
        atime=Label(movie,text="Enter new time:",font=("Arial",15),fg="black",bg="light blue")
        atime.place(x=30,y=160-30)
        afdate=Label(movie,text="(HH:MM:SS)",font=("Arial",15),fg="black",bg="light blue")
        afdate.place(x=30,y=185-30)
        tim=Entry(movie,textvariable=StringVar(),font=("Arial",12))
        tim.place(x=200,y=160-30,height=30,width=200)
        
        updatem=Button(movie, text = "update" ,font='Verdana 10 bold', command=action,width=8,height=2)
        updatem.place(x=200,y=220-30)
        movie.mainloop()