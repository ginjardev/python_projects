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
        snd.read('sound.wav')
        snd.play(blocking=1)
        break


def actual_time():
    set_alarm_timer = f"{hour.hour}:{hour.minute}:{hour.second}"
    alarm(set_alarm_timer)


#clock gui 

clock.title("Alarm Clock")
clock.geometry('400x200')
time_format = Label(clock, text="Enter time in 24 hour format!", fg="green", bg="black", font="Arial").place(x=60, y=120)
add_time = Label(clock, text="Hour Min Sec", font=60).place(x=110)
set_your_alarm = Label(clock, text="When to wake you up", fg="blue", relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)


hour = StringVar()
min = StringVar()
sec = StringVar()




clock.mainloop()