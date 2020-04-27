 
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
        correct_letters = []
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
            if len(correct_letters) == len(word):
                done = True
                print("Congratulations, you won!")
            elif guesses_left==0:
                done = True
                print("Sorry, you lost!")
            else:
                for i in range(len(word)):
                     if(word[i] in guessed_letters):
                         print(word[i])
                     else:
                         print('__')
               letter = input("Enter a letter: ")
        want_to_play = input("Would you like to play another game? [Y]es or [N]o")



if __name__ == '__main__':
    play_hangman()
