from email import message
from tkinter import *
# from tkinter import messagebox
import random
from tkinter import messagebox


target = 0
score = 10
guess = 0

def add():
    return "The sum of target and guess is:" + str(guess + target)

def sub():
    return "The difference of target and guess is:" + str(target - guess)

def multiplication():
    return "The product of target and guess is:" + str(target * guess)

def division():
    return "The quotient of target and guess is:" + str(target / guess)

def greater_lesser():
    if target < guess:
        return "The target is less than the guess"
    elif target > guess:
        return "The target is greater than the guess"


def clues():
    switcher = {
        0: add(),
        1: sub(),
        2: multiplication(),
        3: division(),
        4: greater_lesser()
    }
    return switcher.get(random.randint(0, 4))


def generate_target_number():
    global target
    target = random.randint(1,10)
    messagebox.showinfo(message="Random Number Generated; Start Guessing!! STARTING SCORE=10")
    random_number_button['state'] = DISABLED
    guess_button['state'] = NORMAL


def guess_and_score():
    global score
    global guess

    try:
        guess = 0
        guess = int(guess_entry.get())
    except:
        messagebox.showerror(message="Please enter a valid number")
        return
    
    if guess == target:
        messagebox.showinfo(message="Congratulations!!! You guessed the number correct. Your score is "+str(score))
        random_number_button['state'] = NORMAL
        guess_button['state'] = DISABLED
    elif score == 0:
        messagebox.showinfo(message="Out of guesses buddy. Better luck next time")
        return
    else:
        score -= 1
        message = clues()
        messagebox.showinfo(message=message)


root = Tk()
root.title("Number Guessing Game")
root.geometry("500x500")

Label(root, text="Number guessing game \nGuess a number between 1 and 10", font="ubunto Mono 12").pack()

