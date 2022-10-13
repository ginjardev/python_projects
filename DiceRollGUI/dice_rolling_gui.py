import tkinter
from PIL import Image, ImageTk
import random


root = tkinter.Tk()
root.geometry("400x400")
root.title("Dice Rolling Simulator")

# Adding label into the frame
Blankline = tkinter.Label(root,text="")
Blankline.pack()

# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Hello dice-roll player",
fg = "light green",
bg = "dark green",
font="Helvetica 16 bold italic")
HeadingLabel.pack()


#add images
dice = ['die1.svg', 'die2.svg', 'die3.svg','die4.svg', 'die5.svg', 'die6.svg']

# simulate dice with random numbers from 0 - 6 with images
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))


# #construct a label widget for image
# ImageLabel = tkinter.Label(root, image=DiceImage)
# ImageLabel.image = DiceImage

# ImageLabel.pack(expand=True)