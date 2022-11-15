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
search = StringVar()

# the functions
def submit_record(): 
    global name, email, phone, address_entry
    global cursor
    name, email, phone, address = name.get(), email.get(), phone.get(), address_entry.get(1.0, END)

    if name == '' or email == '' or phone == '' or address == '':
        messagebox.showerror('Error!', 'Please fill all the fields')
    else:
        cursor.execute(
            "INSERT INTO CONTACT_BOOK (NAME, EMAIL, PHONE_NUMBER, ADDRESS) VALUES (?, ?, ?, ?)", (name, email, phone, address)
        )
        connector.commit()
        messagebox.showinfo('Contact added, contact stored successfully')
        listbox.delete(0, END)
        list_contacts()
        clear_fields()


def list_contacts():
    curr = connector.execute('SELECT NAME FROM CONTACT_BOOK')
    fetch = curr.fetchall()


def delete_record():
    global listbox, connector, cursor

    if not listbox.get(ACTIVE):
        messagebox.showerror("No item selected, you have not selected any item")
    
    cursor.execute('DELETE FROM CONTACT_BOOK WHERE NAME= ?', (listbox.get(ACTIVE)))
    connector.commit()

    messagebox.showinfo("Contact Deleted")
    listbox.delete(0,END)
    list_contacts()


def delete_all_records():
    cursor.execute('DELETE FROM CONTACT_BOOK')
    connector.commit()

    messagebox.showinfo("All records deleted")
    listbox.delete(0, END)
    list_contacts()


def view_record():
    global name, phone, email, address_entry, listbox

    curr = cursor.execute(
        "SELCT FROM CONTACT_BOOK WHERE NAME = ?", listbox.get(ACTIVE)
    )
    values = curr.fetchall()[0]

    name.set(values[1]); phone.set(values[3]); email.set(values[2])

    address_entry.delete(1.0, END)
    address_entry.insert(END, values[4])


def clear_fields():
    global name, phone, email, address_entry, listbox

    listbox.select_clear(0, END)

    name.set("")
    phone.set("")
    email.set("")
    address_entry.delete(1.0, END)


def search_record():
    query = str(search.get())

    if query != '':
        listbox.delete(0, END)

        curr = connector.execute(
            "SELECT * FROM CONTACT_BOOK WHERE NAME= ?", ('%'+query+'%', )
        )
        check = curr.fetchall()

        for data in check:
            listbox.insert(END, data[1])




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


Label(left_frame, text='Phone No.', bg=lf_bg, font=frame_font).place(relx=0.23, rely=0.2)

phone_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=phone)
phone_entry.place(relx=0.1, rely=0.25)

Label(left_frame, text="Email", bg=lf_bg, font=frame_font).place(relx=0.3, rely=0.35)

email_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=email)
email_entry.place(relx=0.1, rely=0.4)

Label(left_frame, text="Address", bg=lf_bg, font=frame_font).place(relx=0.28, rely=0.5)

address_entry = Text(left_frame, width=15, font=("Verdana", 11), height=5)
address_entry.place(relx=0.1, rely=0.55)

# middle frame
# Label(center_frame, text="Search", font=frame_font, bg=cf_bg).place(relx=0.3, rely=0.03)
search_entry = Entry(center_frame, width=18, font=("Verdana", 12), textvariable=search).place(relx=0.06, rely=0.04)

Button(center_frame, text="Search", font=frame_font, width=13, command=search_record).place(relx=0.05, rely=0.1)
Button(center_frame, text="Add Record", font=frame_font, width=13, command=submit_record).place(relx=0.05, rely=0.2)
Button(center_frame, text="View Record", font=frame_font, width=13, command=view_record).place(relx=0.05, rely=0.3)
Button(center_frame, text="Clear Fields", font=frame_font, width=13, command=clear_fields).place(relx=0.05, rely=0.4)
Button(center_frame, text="Delete Record", font=frame_font, width=13, command=delete_record).place(relx=0.05, rely=0.5)
Button(center_frame, text="Delete All Records", font=frame_font, width=14, command=delete_all_records).place(relx=0.04, rely=0.6)

# right frame
Label(right_frame, text="Saved Contacts", font=("Roboto", 14), bg=rf_bg).place(relx=0.25, rely=0.05)

listbox = Listbox(right_frame, selectbackground="SkyBlue", bg="green", font=('Helvetica', 12), height=20, width=25)
scroller = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
scroller.place(relx=0.93, rely=0, relheight=1)
listbox.config(yscrollcommand=scroller.set)
listbox.place(relx=0.1, rely=0.15)

list_contacts()



app.mainloop()