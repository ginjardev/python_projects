import tkinter
# from PIL import ImageGrab
import pyscreenshot as ImageGrab
import cv2
import numpy as np
from tkinter import *



def record_screen():
    image = ImageGrab.grab()
    img_np_arr = np.array(image)

    #Extract and print shape of array
    shape = img_np_arr.shape
    # print(shape)

    #create video writer
    screen_cap_writer = cv2.VideoWriter('screen_recorded.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 50, (shape[1], shape[0]))

    #view screen recording on new window
    scale_by_percent = 50
    width = int(shape[1] * scale_by_percent/100)
    height = int(shape[0] * scale_by_percent/100)
    new_dim = (width, height)

    #record screen loop to keep recording
    while True:
        #capture screen
        image = ImageGrab.grab()
        # convert to array
        img_np_arr = np.array(image)
        #conver BGR to RBG
        final_img = cv2.cvtColor(img_np_arr, cv2.COLOR_RGB2BGR)
        screen_cap_writer.write(final_img)

        """
        If you choose to view the screen recording simultaneously,
        It will be displayed and also recorded in your video.
        """

        image = cv2.resize(final_img, (new_dim))
        cv2.imshow("image", image)

        #stop recording on pressing 'x'
        if cv2.waitKey(1) == ord('x'):
            break
    
    
    #release recorded objects
    screen_cap_writer.release()
    cv2.destroyAllWindows()


app = Tk()
app.geometry("340x220")
app.title("Screen Recorder")
# PhotoImage()

title_label = Label(app, text="Screen Recorder", font="Ubuntu 16", bg="#02b9e5")
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

info_label = Label(app, text="Enter 'x' to exit screen recording",bg="#02b9e5")
info_label.place(relx=0.5, rely=0.3, anchor=CENTER)

screen_button = Button(app, text="Record Screen", command=record_screen, relief=RAISED)
screen_button.place(relx=0.5, rely=0.6, anchor=CENTER)

app.mainloop()