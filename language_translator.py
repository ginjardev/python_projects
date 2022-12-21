from tkinter import *
from tkinter import messagebox
import googletrans
from googletrans import Translator

#initialize tkinter
app = Tk()
app.geometry("500x300")
app.title("Language Translator")

translator_object = Translator()

#GUI
title_label = Label(app, text="Language Translator using Python", font=("Roboto", 12))
text_label = Label(app, text="Text to translate: ").place(x=10, y=20)
text_entry = Text(app, width=40, height=5, font=("Ubuntu Mono", 12))
text_entry.place(x=130, y=20)

src_label = Label(app, text="Source Language (empty: auto-detect):").place(x=10, y=120)
src_entry = Text(app, width=20, height=1, font=("Ubuntu Mono",12))
src_entry.place(x=275, y=150)

button1 = Button(app, text="Translate", bg= "Turquiose", command=translate_function).place(x=160, y=190)
button2 = Button(app, text="Clear", bg="Turquoise", command=clear).place(x=270, y=190)



def translate_function():
    pass



app.mainloop()
