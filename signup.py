from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext
import mysql.connector as pymysql

signup_window=Tk()
signup_window.title("instant messaging app")
signup_window.geometry('1000x500+300+200')
signup_window.configure(bg='#000000')
signup_window.resizable(False,False)


def login_page():
    signup_window.destroy()
    import client

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All fields are required >_<')
    elif passwordEntry.get()!= confirmEntry.get():
        messagebox.showerror('Error','Password mismatch -_-')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='123456789')
            cur=con.cursor()
            cur.execute('create user_data')
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(40));'
            cur.execute(query)
            
        except:
            cur=con.cursor()
            cur.execute('use user_data')
            cur.execute('create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(40),timestamp TIMESTAMP);')
            

        query="insert into data(email,username,password) values(%s,%s,%s)"
        cur.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Registration in successful')
        clear()
        signup_window.destroy()
        
background=PhotoImage(file='./signup.png',master=signup_window)
Image_label=Label(signup_window,image=background,border=0,bg='#000000').place(x=50,y=90)

frame=Frame(signup_window,bg="#000000")
frame.place(x=554,y=100)


heading=Label(frame,text='SIGN UP',fg="#8c61ff",bg='#000000',font=('Microsoft Yahei UI Light',23,'bold'))
heading.grid(row=0,column=0,padx=10,pady=10)

emaillabel=Label(frame,text="Email",font=('Microsoft Yahei UI Light',12,'bold'),bg='#000000',fg='#fff')
emaillabel.grid(row=1,column=0,sticky='w',padx=25)

emailEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='#fff',bg='#000000')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernamelabel=Label(frame,text="Username",font=('Microsoft Yahei UI Light',12,'bold'),bg='#000000',fg='#fff')
usernamelabel.grid(row=3,column=0,sticky='w',padx=25)

usernameEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='#fff',bg='#000000')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordlabel=Label(frame,text="password",font=('Microsoft Yahei UI Light',12,'bold'),bg='#000000',fg='#fff')
passwordlabel.grid(row=5,column=0,sticky='w',padx=25)

passwordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='#fff',bg='#000000')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)
passwordEntry.config(show='*')

confirmlabel=Label(frame,text="confirm password",font=('Microsoft Yahei UI Light',12,'bold'),bg='#000000',fg='#fff')
confirmlabel.grid(row=7,column=0,sticky='w',padx=25)

confirmEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='#fff',bg='#000000')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)
confirmEntry.config(show='*')

signupbutton=Button(frame,text='signup',font=('Microsoft Yahei UI Light',9,'bold'),bd=0,bg='#57a1f8',fg='#fff',command=connect_database)
signupbutton.grid(row=10,column=0,padx=25)

alreadyaccount=Label(frame,text="did'nt signin?",font=('Open Sans',9,'bold'),bg='#000000',fg='#fff')
alreadyaccount.grid(row=14,column=0,sticky='w',padx=25)

loginbutton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),bg='#000000',fg='#57a1f8',bd=0,cursor='hand2',activebackground='#000000',activeforeground='#57a1f8',command=login_page)
loginbutton.grid(row=14,column=0,padx=25)

signup_window.mainloop()
