import sqlite3 as sql
from tkinter import *
from tkinter import messagebox


try:
    connect = sql.connect('note.db')
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE notes_table
                        (date text, notes_title text, notes text)''')
except:
    print('Connected to table of database')


def add_notes():
    today = date_entry.get()
    notes_title = notes_title_entry.get()
    notes = notes_entry.get('1.0', 'end-1c')

    if(len(today) <= 0) and (len(notes_title) <= 0) and (len(notes) <= 1):
        messagebox.showerror(message="Enter some details")
    else:
        cursor.execute("INSERT INTO notes_table VALUES ('%s','%s','%s')" %(today, notes_title, notes))
        messagebox.showinfo(message="Note added")
        connect.commit()


def view_notes():
    date = date_entry.get()
    notes_title = notes_title_entry.get()

    if (len(date) <= 0) and (len(notes_title)<=0):
        sql_statement = "SELECT * FROM notes_table"
    elif (len(date)<= 0) and (len(notes_title) > 0):
        sql_statement = "SELECT * FROM notes_table where notes_title = '%s" %notes_title
    elif (len(date) > 0) and (len(notes_title) <= 0):
        sql_statement = "SELECT * FROM notes_table where date = '%s'" %date
    else: 
        sql_statement = "SELECT * FROM notes_table where date ='%s' and notes_title ='%s'" %(date, notes_title)

    cursor.execute(sql_statement)
    row = cursor.fetchall()

    if len(row) <= 0:
        messagebox.showerror(message="No note found")
    else: 
        for i in row:
            messagebox.showinfo(message="Date: " + i[0] + "\nTitle: "+ i[1] + "\nNotes: " + i[2])



def delete_notes():
    date = date_entry.get()  
    notes_title = notes_title_entry.get()
    choice = messagebox.askquestion(message="Do you want to delete all notes?")

    if choice == 'yes':
        sql_statement = "DELETE FROM notes_table"
    else: 
        if(len(date) <= 0) and (len(notes_title) <= 0):
            messagebox.showerror(message="ENTER REQUIRED DETAILS")
        else: 
            sql_statement = "DELETE FROM notes_table where date ='%s' and notes_title ='%s'" %(date, notes_title)

    cursor.execute(sql_statement)
    messagebox.showinfo(message="Note(s) Deleted")
    connect.commit()


def update_notes():
    today = date_entry.get()
    notes_title = notes_title_entry.get()
    notes = notes_entry.get('1.0', 'end-1c')

    if (len(today) <= 0) and (len(notes_title) <= 0) and (len(notes) <= 1):
        messagebox.showerror(message="Enter required details")
    else:
        sql_statement = "UPDATE notes_table SET notes = '%s' where date ='%s' and notes_title ='%s'" %(notes, today, notes_title)

    cursor.execute(sql_statement)
    messagebox.showinfo(message="Note Updated")
    connect.commit()


#notes gui
window = Tk()

window.geometry('600x400')
window.title('Pin Your Note')

title_label = Label(window, text="Pin Your Note").pack()

date_label = Label(window, text="Date: ").place(x=10, y=20)
date_entry = Entry(window, width=20)
date_entry.place(x=90, y=20)

notes_title_label = Label(window, text="Notes Title: ").place(x=10, y=50)
notes_title_entry = Entry(window, width=40)
notes_title_entry.place(x=90, y=50)

notes_label = Label(window, text="Notes: ").place(x=10, y=90)
notes_entry = Text(window, width=60, height=5)
notes_entry.place(x=90, y=90)

#buttons
button1 = Button(window, text= 'Add Notes', bg="green", fg="White", command=add_notes).place(x=10,y=190)
button2 = Button(window, text= 'View Notes', bg="grey", fg="White", command=view_notes).place(x=115,y=190)
button3 = Button(window, text= 'Delete Notes', bg="red", fg="White", command=delete_notes).place(x=235,y=190)
button4 = Button(window, text= 'Update Notes', bg="blue", fg="White", command=update_notes).place(x=360,y=190)

window.mainloop()
connect.close()