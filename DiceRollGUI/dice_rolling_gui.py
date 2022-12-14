import tkinter
from PIL import Image, ImageTk
import random


root = tkinter.Tk()
root.geometry("800x800")
root.title("Dice Rolling Simulator")

# Adding label into the frame
Blankline = tkinter.Label(root,text="")
Blankline.pack()

# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Welcome Player!", width=17, height=2,
fg = "white",
bg = "dark grey",
font="Roboto 16 bold")
HeadingLabel.pack()

#add images
dice = ['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

#packing a widget in the parent widget
ImageLabel.pack(expand=True)


# function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    #update image
    ImageLabel.configure(image=DiceImage)
    #reference
    ImageLabel.image = DiceImage

button = tkinter.Button(root, text="Roll Dice", bg="grey", fg="white", 
command=rolling_dice,
font="Roboto 12 bold")

# pack a widget in the parent widget
button.pack(expand=True)


# call the mainloop of Tk
root.mainloop()