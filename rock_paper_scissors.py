from tkinter import *
import random


root = Tk()
root.geometry('500x400')
root.resizable(0,0)
root.title("Rock Paper Scissors")
root.config(bg="seashell3")


Label(root, text="Rock, Paper, Scissors", font="arial 20 bold", bg="seashell3").pack()

user_take = StringVar()

Label(root, text="Choose One: Rock, Paper, Scissors", font= 'Roboto 15 bold', bg='seashell2').place(x = 20,y=70)
Entry(root, font="arial 15", textvariable=user_take, bg="antiquewhite2", ).place(x=90 , y = 130)

computer_choice = random.randint(1,3)
if computer_choice == 1:
    computer_choice = 'rock'
elif computer_choice == 2:
    computer_choice = 'paper'
else: 
    computer_choice = 'scissors'


result = StringVar()

def play():
    user_pick = user_take.get()
    user_pick = user_pick.lower()
    
    if user_pick == computer_choice:
        result.set("tie, you both picked same")
    elif user_pick == 'rock' and computer_choice == 'paper':
        result.set("You lose, computer picked paper")
    elif user_pick == 'rock' and computer_choice == 'scissors':
        result.set("You win, computer picked scissors")
    elif user_pick == 'paper' and computer_choice == 'scissors':
        result.set("You lose, computer picked scissors")
    elif user_pick == 'paper' and computer_choice == 'rock':
        result.set("You win, computer picked rock")
    elif user_pick == 'scissors' and computer_choice == 'rock':
        result.set("You lose, computer picked rock")
    elif user_pick == 'scissors' and computer_choice == 'paper':
        result.set("You win, computer picked paper")
    else:
        result.set("Invalid, choose: rock, paper or scissors")


def reset():
    result.set("")
    user_take.set("")

def exit():
    root.destroy()


Entry(root, font="Roboto 10 bold", textvariable=result, bg='antiquewhite2', width=50).place(x=20, y = 250)
Button(root, font='Roboto 13 bold', text='Play', padx=5, bg='seashell4', command=play).place(x=150,y=190)
Button(root, font="Roboto 13 bold", text='Reset', padx=5, bg='seashell4', command=reset).place(x=70,y=310)
Button(root, text="Exit", font="Roboto 13 bold", padx=5, bg='seashell4', command=exit).place(x=230,y=310)

root.mainloop()