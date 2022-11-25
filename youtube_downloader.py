from tkinter import *
from tkinter import messagebox
from pytube import YouTube

app = Tk()
app.geometry('580x300')
app.resizable(0,0)
app.title("YouTube Downloader")

Label(app, text="YouTube Downloader", font="Roboto 17 bold").pack()

link = StringVar()

Label(app, text='Paste link below', font='arial 14 bold').place(x= 180 , y = 60)
link_entry = Entry(app, width=70, textvariable=link).place(x = 5, y = 90)


def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download('/home/ini/Downloads')
    messagebox.showinfo('Status',"Video downloaded")
    # Label(app, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210) 

    
def reset():
    link.set("")

Button(app, text="Download", font="arial 15 bold", bg="lightblue", padx=2, command=downloader).place(x=100,y = 150)
Button(app, text="Reset", font="arial 15 bold", bg="grey", padx=2, command=reset).place(x=260 ,y = 150)
    

app.mainloop()