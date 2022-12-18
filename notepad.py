from tkinter import *
from tkinter import font, filedialog


app = Tk()
app.title("Python Text Editor")

text_area = Text(app)
text_area.grid(row=2, columnspan=5)


def save_doc():
    global text_area
    text = text_area.get("1.0", "end-1c")
    location = filedialog.asksaveasfilename()
    file = open(location, "w+")
    file.write(text)
    file.close()


def algerian():
    global text_area
    text_area.config(font="Algerian")

def arial():
    global text_area
    text_area.config(font="Arial")


def courier():
    global text_area
    text_area.config(font="Courier")


def cambria():
    global text_area
    text_area.config(font="Cambria")

def bold_doc():
    global text_area
    text_area.config(font=('arial', 14, 'bold'))

save_btn = Button(app, command=save_doc, text="Save")
save_btn.grid(row=1, column=0)
save_btn.config(font=('arial', 20, 'bold'), bg="DodgerBlue2", fg="white")

font_btn = Menubutton(app, text="Font")
font_btn.grid(row=1, column=1)
font_btn.config(font=('arial', 20, 'bold'), bg="DodgerBlue2", fg="white")
font_btn.menu = Menu(font_btn, tearoff=0)
font_btn["menu"] = font_btn.menu

font_btn.menu.add_checkbutton(label="Arial", command=arial)
font_btn.menu.add_checkbutton(label="Algerian", command=algerian)
font_btn.menu.add_checkbutton(label="Cambria", command=cambria)
font_btn.menu.add_checkbutton(label="Courier", command=courier)

bold_btn = Button(app, command=bold_doc, text="Bold")
bold_btn.grid(row=1, column=2)
bold_btn.config(font=('arial', 20, 'bold'), bg="DodgerBlue2", fg="white")



