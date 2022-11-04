from tkinter import *
import datetime
import time
# import winsound
import tkSnack




clock = Tk()
tkSnack.initializeSnack(clock)

hour = datetime.datetime.now()
print(hour.hour)

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is: ", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to wake up")
        #winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        global tkSnack
        snd = tkSnack.Sound()
        snd.read('dripchord.wav')
        snd.play(blocking=1)
        break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


#clock gui 

clock.title("Alarm Clock")
clock.geometry('400x300')
time_format = Label(clock, text="Enter time in 24 hour format!", fg="green", bg="black", font="Arial").place(x=60, y=120)
add_time = Label(clock, text="Hour Min Sec", font=60).place(x=110)
Label(clock, text='').pack()
set_your_alarm = Label(clock, text="When to wake you up", fg="blue", relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)


hour = StringVar()
min = StringVar()
sec = StringVar()


hourTime = Entry(clock, textvariable= hour, bg="pink", width=15).place(x=110, y=30)
minTime = Entry(clock, textvariable=min, bg="pink", width=15).place(x=150, y=30)
secTime = Entry(clock, textvariable=sec, bg="pink", width=15).place(x=200, y=30)

submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time).place(x=110, y=70)


clock.mainloop()