from tkinter import*
import tkinter as tk



window=tk.Tk()
window.title("instant messaging app - Menu")
window.geometry('1000x500+300+200')
window.configure(bg='#000000')
window.resizable(False,False)



background=PhotoImage(file='./signup.png')
Image_label=Label(image=background,border=0,bg='#000000').place(x=50,y=90)

frame=Frame(window,bg="#000000")
frame.place(x=554,y=100)

def client():
    import client
def translator():
    import language_translator
def spelling():
    import spellingcorrector
def exit1():
    window.destroy()


heading=Label(frame,text='MENU',fg='#EA047E',bg='black',font=('Microsoft Yahei UI Light',23,'bold'))
heading.grid(row=0,column=0,padx=0,pady=0)


clientButton=Button(frame,text='Client',font=('Open Sans',18,'bold'),bg='#EA047E',fg='#fff',command=client)
clientButton.place(x=500,y=150)

spellingButton=Button(frame,text='Spelling Corrector',font=('Open Sans',18,'bold'),bg='#EA047E',fg='#fff',command=spelling)
spellingButton.place(x=500,y=230)

langButton=Button(frame,text='Language Translator',font=('Open Sans',18,'bold'),bg='#EA047E',fg='#fff',command=translator)
langButton.place(x=500,y=310)

exitButton=Button(frame,text='EXIT',font=('Open Sans',18,'bold'),bg='#EA047E',fg='#fff',command=exit1)
exitButton.place(x=500,y=390)

window.mainloop()