from tkinter import *
from tkinter import messagebox
import string
import pyperclip
import random


window = Tk()
window.geometry('400x400')
window.resizable(0,0)
window.title("Password Generator")


Label(window, text="Password Generator", font='arial 15 bold').pack()
Label(window, text="GreyLoop", font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(window, text="Password Length", font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(window, from_=8, to_ = 32, textvariable=pass_len, width=15).pack()

pass_str = StringVar()


def generator():
    password = ''

    for x in range(0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    
    for y in range(pass_len.get() - 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    
    pass_str.set(password)


Button(window, text="Gnerate Password", command=generator).pack(pady=5)
Entry(window, textvariable=pass_str).pack()


def copy_password():
    pyperclip.copy(pass_str.get())
    messagebox.showinfo(message="password copied!")
    

Button(window, text='Copy to clipboard', command=copy_password).pack()

window.mainloop()