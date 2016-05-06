#A reverse number guessing game in Python

import random

#Game Loop
reply='Y'

while reply == 'Y':
    my_num = input("Enter your number: ")
    try:
        num = int(my_num)
    except ValueError:
        print("Not an integer.Please enter an integer.")
    else:
        num_of_guess = 3
        i = 1
        j = 10
        while True:
            comp_guess = random.randint(i,j)
            if comp_guess == num:
                print("Computer has guessed your number correctly. The number is: " + str(comp_guess))
                break
            elif comp_guess > num:
                print("The guess is greater than my number.")
                print("The computer guessed incorrectly: " + str(comp_guess))
                print("")
                i = i
                j = comp_guess-1
                num_of_guess -= 1
            elif comp_guess < num:
                print("The guess is less than my number.")
                print("The computer guessed incorrectly: " + str(comp_guess))
                print("")
                i = comp_guess + 1
                j = j
                num_of_guess -= 1
            if num_of_guess == 0:
                print("Computer was unable to guess your number. Your number was: " + str(num))
                break
        reply = input("Do you want the computer to start with guessing game again? Y/N ")
            
        
    
    
