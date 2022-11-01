from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext
import ast
import socket
import threading
import tkinter as tk
import mysql.connector as pymysql


signup_window=Tk()
signup_window.title("instant messaging app")
signup_window.geometry('1000x500+300+200')
signup_window.configure(bg='#000000')
signup_window.resizable(False,False)
signup_window.overrideredirect(True)


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
            con=pymysql.connect(host='localhost',user='root',password='123456789',database='user_data')
            cur=con.cursor()
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(40));'
            cur.execute(query)
            
        except:
            con=pymysql.connect(host='localhost',user='root',password='123456789',database='user_data')
            cur=con.cursor()
            cur.execute('use user_data')
            #cur.execute('create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(40));')
            

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

signup_window.mainloop()

s=socket.socket()
HOST = socket.gethostname()
PORT =1234


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

