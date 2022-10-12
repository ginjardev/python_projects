from itertools import count
import random
import time

print("Welcome to Hangman!")
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman, best of luck!")
time.sleep(2)
print("The game is about to start, let's go!")
time.sleep(3)


# variables for the game
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["rainbow", "computer", "science", "programming", "python", "mathematics", "player", "condition", "reverse", "water", "board", "geeks"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""



# function to play the game
def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no \n")

    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do you want to play again? y = yes, n = no \n")
    
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing! See you next time.")
        exit()



# initializing all the conditions reguired for the game

def hangman():
    global count
    global display 
    global word
    global already_guessed
    global play_game
    limit = 5 

    guess = input("This is the hangman word: " + display + " Enter your guess: \n")
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9": 
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1 

        if count == 1:
            time.sleep(1)
            print("  _____ \n"
                  " |      \n"
                  " |      \n"
                  " |      \n"
                  " |      \n"
                  " |      \n"
                  " |      \n"
                  "_|___   \n")
            print("Wrong guess. " + str(limit - count) + " guesses left\n")

        elif count == 2:
            time.sleep(1)
            print("  _____ \n"
                  " |     | \n"
                  " |     | \n"
                  " |      \n"
                  " |      \n"
                  " |      \n"
                  " |      \n"
                  "_|___   \n")
            print("Wrong guess. " + str(limit - count) + " guesses left\n")

        elif count == 3:
            time.sleep(1)
            print("  _____ \n"
                  " |     | \n"
                  " |     | \n"
                  " |     | \n"
                  " |      \n"
                  " |      \n"
                  " |      \n"
                  "_|___   \n")
            print("Wrong guess. " + str(limit - count) + " guesses left\n")

        elif count == 4:
            time.sleep(1)
            print("  _____ \n"
                  " |     | \n"
                  " |     | \n"
                  " |     | \n"
                  " |     O \n"
                  " |      \n"
                  " |      \n"
                  "_|___   \n")
            print("Wrong guess. " + str(limit - count) + " last guess\n")

        elif count == 5:
            time.sleep(1)
            print("  _____ \n"
                  " |     | \n"
                  " |     | \n"
                  " |     | \n"
                  " |     O \n"
                  " |    /|\ \n"
                  " |    / \ \n"
                  "_|___   \n")
            print("Wrong guess. You are hanged!\n")
            print("The word was:", already_guessed, word)
            play_loop()

        if word == '_' * length:
            print("Congrats! You have guessed the word correctly!")
            play_loop()
        
        elif count != limit:
            hangman()


# calling the main function
main()

# calling the hangman function
hangman()
play_loop()