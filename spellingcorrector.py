import tkinter
from tkinter import *
from textblob import TextBlob
root=Tk()
root.title("spelling corrector")
root.geometry("700x400")
root.config(background="#000000")

def check_spelling():
  word=enter_text.get()
  a=TextBlob(word)
  right=str(a.correct())

  cs=Label(root,text="correct text is :",font=("poppins",20),bg="#000000", fg="#fff")
  cs.place(x=100,y=250)
  spell.config(text=right)

heading=Label(root,text="spelling corrector",font=("trebuchet MS",30,"bold","italic"),bg="#000000",fg="#fff")
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="center",width=30,font=("poppins",25),bg="black",fg="#fff",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root,text="check",font=("arial",20,"bold"),fg="white",bg="red",command=check_spelling)
button.pack()

spell=Label(root,font=("poppins",20),bg="#000000", fg="#fff")
spell.place(x=350,y=250)

root.mainloop()
