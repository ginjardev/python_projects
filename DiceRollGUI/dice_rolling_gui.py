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
dice = ['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']
resized_imgs = []
for img in dice:
    img = Image.open(img)
    img = img.resize((50,50), Image.ANTIALIAS)
    resized_imgs.append(ImageTk.PhotoImage(img))
# simulate dice with random numbers from 0 - 6 with images
DiceImage = random.choice(resized_imgs)


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

button = tkinter.Button(root, text="Roll Dice", fg="blue", command=rolling_dice)

# pack a widget in the parent widget
button.pack(expand=True)


# call the mainloop of Tk
root.mainloop()