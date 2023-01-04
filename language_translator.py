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

dest_label = Label(app, text="Target language (empty: english-default):").place(x=10,y=150)
dest_entry = Text(app, width=20,height=1,font=("Ubuntu Mono",12))
dest_entry.place(x=300,y=150)





def translate_function():
    if(len(src_entry.get("1.0", "end-1c")) > 1):
        src_v = src_entry.get("1.0", "end-1").lower()
        src_v = src_v.replace(" ", "")
    else:
        src_v = None

    if(len(dest_entry.get("1.0", "end-1c")) > 1):
        dest_v = dest_entry.get("1.0", "end-1c").lower()
        dest_v = dest_v.replace(" ", "")
    else:
        dest_v = None

    if(len(text_entry.get("1.0", "end-1c")) <= 1):
        messagebox.showerror(message="Enter valid text")
    else:
        text_v = text_entry.get("1.0", "end-1c")
        if (not src_v) & (not dest_v):
            translated_text = translator_object.translate(text_v)
        elif (not src_v):
            translated_text = translator_object.translate(text_v, dest=dest_v)
        elif (not dest_v):
            translated_text = translator_object.translate(text_v, src=src_v)
        else:
            translated_text = translator_object.translate(text_v, src=src_v, dest=dest_v)
        
        messagebox.showinfo(message="Translated Text: "+ translated_text.text)


def clear():
    dest_entry.delete("1.0", "end-1c")
    src_entry.delete("1.0", "end-1c")
    text_entry.delete("1.0", "end-1c")

button1 = Button(app, text="Translate", bg= "cyan", command=translate_function).place(x=160, y=190)
button2 = Button(app, text="Clear", bg="cyan", command=clear).place(x=270, y=190)

app.mainloop()

print(googletrans.LANGUAGES)