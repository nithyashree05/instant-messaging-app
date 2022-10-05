from tkinter import*
from tkinter import messagebox

login_window=Tk()
login_window.geometry('975x615+300+200')
login_window.configure(bg='#000000')
login_window.resizable(False,False)

def signup_page():
    login_window.destroy()
    import messaging

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


image1=PhotoImage(file=r"C:\python instant messaging\login.png")
label1=Label(image=image1,bg="#000000").place(x=50,y=50)

heading=Label(login_window,text="SIGN IN",font=('Microsoft Yahei UI Light',29,'bold'),bg='#000000',fg='#8c61ff')
heading.place(x=610,y=100)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,bg='#000000',fg='#fff')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2)
frame1.place(x=580,y=222)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,bg='#000000',fg='#fff')
passwordEntry.place(x=580,y=290)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2)
frame2.place(x=580,y=312)



loginButton=Button(login_window,text='Login',font=('Open Sans',17,'bold'),bg='#57a1f8',fg='#fff',activebackground='#57a1f8',activeforeground='#fff')
loginButton.place(x=655,y=390)

signuplabel=Label(login_window,text='Didnt sign up?',font=('Open Sans',11,'bold'),fg='white',bg='black')
signuplabel.place(x=590,y=500)


newaccountbutton=Button(login_window,text='Create New one',font=('Open Sans',9,'bold underline'),fg='white',bg='#57a1f8',activeforeground='white',activebackground='#57a1f8',cursor='hand2',bd=0,command=signup_page)
newaccountbutton.place(x=727,y=500)                        





login_window.mainloop()
