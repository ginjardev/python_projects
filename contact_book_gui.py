from tkinter import *
from tkinter import messagebox
import sqlite3 as sql


connector = sql.connect('contacts.db')
cursor = connector.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS CONTACT_BOOK (S_NO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, EMAIL TEXT, PHONE_NUMBER TEXT, ADDRESS TEXT)"
)


app = Tk()
app.title("Contact Book GUI")
app.geometry('700x500')
app.resizable(0,0)

#color and font variables
lf_bg = "Gray70"
cf_bg = "Gray57"
rf_bg = "Gray35"
frame_font = ("Garamond", 14)

# StringVar variables
name = StringVar()
phone = StringVar()
email = StringVar()


Label(app, text="Contact Book", font=("Roboto", 15, "bold"), bg="Black", fg="White").pack(side=TOP, fill=X)

left_frame = Frame(app, bg=lf_bg)
left_frame.place(relx=0, relheight=1, y=30, relwidth=0.3)


center_frame = Frame(app, bg=cf_bg)
center_frame.place(relx=0.3, relheight=1, y=30, relwidth=0.3)


right_frame = Frame(app, bg=rf_bg)
right_frame.place(relx=0.6, relwidth=0.4, relheight=1, y=30)


# components left frame
Label(left_frame, text='Name', bg=lf_bg, font=frame_font).place(relx=0.3, rely=0.05)

name_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=name)
name_entry.place(relx=0.1, rely=0.1)


Label(left_frame, text='Phone No.', bg=lf_bg, font=("Verdana", 11), textvariable=phone).place(relx=0.23, rely=0.2)

phone_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=phone)
phone_entry.place(relx=0.1, rely=0.25)

Label(left_frame, text="Email", bg=lf_bg, font=frame_font).place(relx=0.3, rely=0.35)

email_entry = Entry(left_frame, width=15, font=("Verdana", 11))
