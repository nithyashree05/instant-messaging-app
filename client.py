from tkinter import*
from tkinter import messagebox
import ast
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

root=window=Tk()
root.title("instant messaging app")
root.geometry('925x500+300+200')
root.configure(bg='#000000')
root.resizable(False,False)



def signin():
  username=user.get()
  password=code.get()

  file=open(r'C:/python instant messaging/datasheet.txt')
  d=file.read()
  r=ast.literal_eval(d)
  file.close()
  
  if username in r.keys() and password==r[username]:
    messagebox.showinfo('thanks!','successfully registered')
    window.destroy()

  else:
    messagebox.showerror('Invalid','Invalid username or password')
#######################################-
def signup_command():
  window=Toplevel(root)
  window.title("SIGNUP")
  window.geometry('925x500+300+200')
  window.configure(bg='#000000')
  window.resizable(False,False)

  def signup():
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()
    if password==confirm_password:
      try:
        file=open('C:/python instant messaging/datasheet.txt','r+')
        d=file.read()
        r=ast.literal_eval(d)
        dict1={username:password}
        r.update(dict1)
        file.truncate(0)
        file.close()

        file=open('C:/python instant messaging/datasheet.txt','w')
        w=file.write(str(r))

        messagebox.showinfo('Signup','Successfully sign up')
        window.destroy()
      except:
        file=open(r'C:/python instant messaging/datasheet.txt','w')
        pp=str({'Username':'password'})
        file.write(pp)
        file.close()
    else:
        messagebox.showerror('Invalid',"Both Password should match")

  def sign():
    window.destroy()

            

  img=PhotoImage(file=r'C:\python instant messaging\signup.png')
  Label(window,image=img,border=0,bg='#000000').place(x=50,y=90)

  frame=Frame(window,width=350,height=390,bg='#000000')
  frame.place(x=480,y=50)

  heading=Label(frame,text='sign up',fg="#8c61ff",bg='#000000',font=('Microsoft Yahei UI Light',23,'bold'))
  heading.place(x=100,y=5)
  
  def on_enter(e):
    user.delete(0,'end')
  def on_leave(e):
    if user.get()=='':
      user.insert(0,'Username')

  user=Entry(frame,width=25,fg='white',border=0,bg='#000000',font=('Microsoft Yahei UI Light',11))
  user.place(x=30,y=80)
  user.insert(0,'Username')
  user.bind("<FocusIn>",on_enter)
  user.bind("<FocusOut>",on_leave)

  Frame(frame,width=295,height=2,bg='white').place(x=25,y=107)

  def on_enter(e):
    code.delete(0,'end')
  def on_leave(e):
    if code.get()=='':
      code.insert(0,'Password')
  code=Entry(frame,width=25,fg='white',border=0,bg='#000000',font=('Microsoft YaHei UI Light',11))
  code.place(x=30,y=150)
  code.insert(0,'Password')
  code.bind("<FocusIn>",on_enter)
  code.bind("<FocusOut>",on_leave)
  Frame(frame,width=295,height=2,bg='white').place(x=25,y=177)

  def on_enter(e):
    confirm_code.delete(0,'end')
  def on_leave(e):
    if confirm_code.get()=='':
      confirm_code.insert(0,'confirm Password')

  confirm_code=Entry(frame,width=25,fg='white',border=0,bg='#000000',font=('Microsoft YaHei UI Light',11))
  confirm_code.place(x=30,y=220)
  confirm_code.insert(0,'confirm password')
  confirm_code.bind("<FocusIn>",on_enter)
  confirm_code.bind("<FocusOut>",on_leave)

  Frame(frame,width=295,height=2,bg='white').place(x=25,y=247)
  Button(frame,width=39,pady=7,text=' Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=282)
  label=Label(frame,text='I have an account',fg='white',bg='black',font=('Microsoft YaHei UI Light',9))
  label.place(x=92,y=346)

  signin=Button(frame,width=6,text='Sign In',border=0,bg='#000000',cursor='hand2',fg='#57a1f8',command=sign)
  signin.place(x=200,y=340)

  window.mainloop()


####################################################################    
img=PhotoImage(file=r"C:\python instant messaging\login.png")
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

sign_up=Button(frame,width=6,text='signup',border=0,bg='#000000',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)


root.mainloop()


###############################################################

s=socket.socket()
HOST = socket.gethostname()
PORT = 1234


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

def connect():

    
    try:

        client.connect((HOST, PORT))
        print("Successfully connected to server")
        add_message("[SERVER] Successfully connected to the server")
    except:
        messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST} {PORT}")

    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
    else:
        messagebox.showerror("Invalid username", "Username cannot be empty")

    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)



def send_message():
    message = message_textbox.get()
    if message != '':
        client.sendall(message.encode())
        message_textbox.delete(0, len(message))
    else:
        messagebox.showerror("Empty message", "Message cannot be empty")

root = tk.Tk()
root.geometry("600x600")
root.title("Client messenger")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

top_frame = tk.Frame(root, width=600, height=100, bg="#121212")
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(root, width=600, height=400, bg="#1F1B24")
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(root, width=600, height=100, bg="#121212")
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

username_label = tk.Label(top_frame, text="Enter username:", font=("Helvetica",17), bg="#121212", fg="#fff")
username_label.pack(side=tk.LEFT, padx=10)

username_textbox = tk.Entry(top_frame, font=("Helvetica",17), bg="#1F1B24", fg="#fff", width=23,)
username_textbox.pack(side=tk.LEFT)

username_button = tk.Button(top_frame, text="Join", font=("Helvetica",15), bg="#8c61ff", fg="#fff", command=connect)
username_button.pack(side=tk.LEFT, padx=15)

message_textbox = tk.Entry(bottom_frame, font=("Helvetica",17), bg="#1F1B24", fg="#fff", width=38)
message_textbox.pack(side=tk.LEFT, padx=10)

message_button = tk.Button(bottom_frame, text="Send", font=("Helvetica",15), bg="#8c61ff", fg="#fff", command=send_message)
message_button.pack(side=tk.LEFT, padx=10)

message_box = scrolledtext.ScrolledText(middle_frame, font=("Helvetica",13), bg="#1F1B24", fg="#fff", width=67, height=26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)


def listen_for_messages_from_server(client):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split('~')[1]

            add_message(f"[{username}] {content}")
            
        else:
            messagebox.showerror("Error", "Message recevied from client is empty")


def main():

    root.mainloop()
    
if __name__ == '__main__':
    main()

