from tkinter import *

app = Tk()
app.geometry('500x300')
app.resizable(2,2)
app.title("Website Blocker")

Label(app, text="Website Blocker", font="arial 20 bold").pack()
Label(app, text="GreyLoop", font="arial 15 bold").pack(side=BOTTOM)


host_path = '/home/ini/Documents/block.txt'
ip_address = '127.0.0.1'

Label(app, text='Enter Website', font='arial 13 bold').place(x=5, y=60)
websites = Text(app, font="arial 10", height=2, width=40, wrap=WORD, padx=5, pady=5)
websites.place(x=140, y=60)


def blocker():
    website_list = websites.get(1.0, END)
    Website = list(website_list.split(','))

    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(app, text="Already Blocked", font='arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(app, text="Blocked", font="arial 12 bold").place(x=230,y =250)


block = Button(app, text = 'Block',font = 'arial 12 bold',pady = 5,command = blocker ,width = 6, bg = 'royal blue', activebackground = 'sky blue')
block.place(x = 230, y = 150)
app.mainloop()