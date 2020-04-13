"""
   Authors: Claire Rousell, Kayla Romero, Maya Rosenfeld, Helen Lin, Veronica Rojas
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""
import random
words="These are some words that we can change later".split()

def generate_random_word():
   """ read a list of words from a file and pick a random one to return """
   return random.choice(words)

def play_hangman():
    want_to_play = True


    while (want_to_play):
        guessed_letters = []
        guesses_left = 6
        word = generate_random_word()
        letter = input("Enter a letter: ")
        done = False
        while not done:
            if letter in guessed_letters:
                guesses_left=guesses_left-1
                print("You already guessed that letter")
            elif letter not in word:
                guessed_letters.append(letter)
                print("The letter is not in the word")
                guesses_left=guesses_left-1
            else:
                guessed_letters.append(letter)
                print("The letter is in the word")
            if "all the letters in the word have been guessed":
                done = True
                print("Congratulations, you won!")
            elif guesses_left=0:
                done = True
                print("Sorry, you lost!")
            else:
                "print the word with a dash for each letter not in guessed_letters"
                letter = input("Enter a letter: ")
        want_to_play = "ask the user if they want to play another game..."


if __name__ == '__main__':
    play_hangman()
