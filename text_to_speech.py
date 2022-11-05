from tkinter import *
from gtts import gTTS
from playsound import playsound


app = Tk()
app.geometry('450x400')
app.configure(bg='ghost white')
app.title('Text To Speech App')

Label(app, text="Text To Speech", font="arail 20 bold", bg="white smoke").pack()
Label(app, text="GreyLoop", font="arial 12 bold", bg="white smoke", width="20").pack(side=BOTTOM)

msg = StringVar()
Label(app, text="Enter Text", font="arial 15 bold", bg="white smoke").place(x=20, y=60)

entry_field = Entry(app, textvariable=msg, width='50',)
entry_field.place(x=20, y=100)


def text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('wording.mp3')
    playsound('wording.mp3')


def exit():
    app.destroy()


def reset():
    msg.set("")


Button(app, text="Play", font='arial 15 bold', command=text_to_speech, width='4', bg='green').place(x=25, y=140)
Button(app, text="Exit", font='arial 15 bold', command=exit, width='4', bg='red').place(x=100, y=140)
Button(app, text="Reset", font='arial 15 bold', command=reset, width='4', bg='orange').place(x=175, y=140)

app.mainloop()