from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("instant messaging app")
window.geometry('925x500+300+200')
window.configure(bg='#000000')
window.resizable(False,False)

def signin():
  username=user.get()
  password=code.get()

  if username=='nsk'and password=='1234':
    mainloop()
  elif username!='nsk'and password!='1234':
    messagebox.showerror("Invalid","invalid username and password")
  elif password!='1234':
    messagebox.showerror("Invalid","invalid password")
  elif username!='admin':
    messagebox.showerror("Invalid","Invalid username")
    
    
img=PhotoImage(file=r"C:/python instant messaging/login.png")
Label(image=img,bg="#000000").place(x=50,y=50)

frame=Frame(width=350,height=350,bg="#000000")
frame.place(x=480,y=70)

heading=Label(frame,text='sign in',fg='#8c61ff',bg='#000000',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

##########-----------------------------------------
def on_enter(e):
  user.delete(0,'end')

def on_leave(e):
  name=user.get()
  if name=='':
    user.insert(0,'Username')
    
user=Entry(frame,width=25,fg='white',border=0,bg="#000000",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="white").place(x=25,y=177)

###########################################################

def on_enter(e):
  code.delete(0,'end')

def on_leave(e):
  name=code.get()
  if name=='':
    code.insert(0,'password')

    
code=Entry(frame,width=25,fg='white',border=0,bg="#000000",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)



Frame(frame,width=295,height=2,bg="white").place(x=25,y=177)


###############################################
Button(frame,width=39,pady=7,text='Signin',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Dont have an account?",fg='white',bg='#000000',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='signup',border=0,bg='#000000',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)


mainloop()


