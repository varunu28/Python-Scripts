#A word guessing game

import random
import os
import sys

words = [
    'apples',
    'banana',
    'lemon',
    'melon',
    'coconut'
    ]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcome():
    start = input("Press Enter to start or Q to quit. ")

    if start == 'Q':
        print("Bye")
        sys.exit()
    return True

def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')
    
    #Draw spaces, guessed letter and strikes
    for letter in secret_word:
        if letter in good_guesses:
            print(letter,end='')
        else:
            print('_',end='')

    

    print('\n\n')
    
    print('')

def get_guess(bad_guesses, good_guesses):
    #Take Guess
    while True:
        guess = input(("Guess a letter: ").lower())
        if len(guess) != 1:
            print("You can guess only a single number")
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guessed this letter")
        elif not guess.isalpha():
            print("You can only guess alphabets")
        else:
            return guess
     
def play(done):
    clear()
    secret_word = random.choice(words)

    
    unique_secret_word = []

    for w in secret_word:
        if w not in unique_secret_word:
            unique_secret_word.append(w)
    
    bad_guesses =[]
    good_guesses =[]

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True

            if len(good_guesses) != len(unique_secret_word):
                found = False
            
            if found:
                print("You win")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("Lost")
                print("The secret word was {}".format(secret_word))
                done = True

        if done:
            play_again = input("Play Again? Y/N: ")
            if play_again == 'Y':
                return play(done = False)
            else:
                sys.exit()
                
        
print("Welcome to letter guessing game")
done = False

while True:
    clear()
    welcome()
    play(done)

