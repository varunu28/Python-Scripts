#A number guessing game in Python

import random

#Generate a random number between 1 and 10
secret_num = random.randint(1,10)

#Game Loop

num_of_guess = 3
reply='Y'

while reply == 'Y':
    guess_num = input("Enter your guess: ")
    try:
        guess = int(guess_num)
    except ValueError:
        print("Not an Integer. Enter an integer as your guess")
    else:
        if guess == secret_num:
            print("You got it")
            reply = input("Do you want to play again? Y/N")
        elif guess < secret_num:
            num_of_guess-=1
            print("That's not it. My number is greater than that")
            print("You have got "+ str(num_of_guess)+ " guesses left.")
        elif guess > secret_num:
            print("That's not it. My number is less than that")
            num_of_guess-=1
            print("You have got "+ str(num_of_guess)+ " guesses left.")
        if num_of_guess == 0:
            print("You lose.")
            reply = input("Do you want to play again? Y/N:  ")
    

    
    
