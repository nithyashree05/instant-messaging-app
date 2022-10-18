from tkinter import*
import tkinter as tk

window=tk.Tk()
window.title("instant messaging app - Menu")
window.geometry('1000x500+300+200')
window.configure(bg='#000000')
window.resizable(False,False)



background=PhotoImage(file='./signup.png',master=window)
Image_label=Label(image=background,border=0,bg='#000000').place(x=50,y=90)


def signup():
    window.destroy()
    import signup
def client():
    window.destroy()
    import client
def translator():
    window.destroy()
    import language_translator
def spelling():
    window.destroy()
    import spellingcorrector
def exit1():
    window.destroy()


heading=Label(window,text='MENU',fg='#EA047E',bg='black',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=650,y=45)

signupButton=Button(window,text='signup',font=('Open Sans',18,'bold'),bg='#EA047E',fg='#fff',command=signup)
signupButton.place(x=575,y=120)

clientButton=Button(window,text='messenger',font=('Open Sans',18,'bold'),bg='#EA047E',fg='#fff',command=client)
clientButton.place(x=575,y=190)

spellingButton=Button(window,text='Spelling Corrector',font=('Open Sans',18,'bold'),bg='#EA047E',fg='#fff',command=spelling)
spellingButton.place(x=575,y=260)

langButton=Button(window,text='Language Translator',font=('Open Sans',18,'bold'),bg='#EA047E',fg='#fff',command=translator)
langButton.place(x=575,y=330)

exitButton=Button(window,text='EXIT',font=('Open Sans',18,'bold'),bg='#EA047E',fg='#fff',command=exit1)
exitButton.place(x=575,y=400)

window.mainloop()
