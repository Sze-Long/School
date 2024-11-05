#Name: Szelong
#Date: April 5th 2024
#purpose: number guessing game

#importing random into program
import random

#creating the main function
def main():
    ran_num = random.randint(1,101)
    guessed = False
    guesses = 0
    while guessed = False:
        guess = int(input("Guess the number!(1-100)"))
        if ran_num == guess:
            print("You guessed the number!")
            guessed = True
        elif ran_num > guess:
            print("Your number too high")
            guesses += 1
        else:
            print("Your number too low")
            guesses += 1
    
        
            
        
