#Name: Sze Long Lam
#Date: April 11th 2024
#Purpose: Guessing number game

#importing random
import random
#Global variables
total_guesses = 15

def main():
    #Greeting
    print("In this game you will guess a number between 1 and 100")

    #creating a random number from 1-100
    #The number has to be at least 10 and stops at 100
    ran_num = random.randrange(10,101,10)
    print(ran_num)

    #user has not guessed the number yet
    guessed = False
    #running total
    counter = 0
    for i in range(total_guesses):
        #user input
        user = int(input("Guess the number between 1-100: "))

        #if their number is not a multiple of 10 between 1- 100
        while (user%10) != 0 or user < 1 or user > 101:
            print("Enter a valid number from 1-100(must be multiple of 10)")
            user = int(input("Guess the number between 1-100: "))

        #their guess couunter goes up by one
        counter += 1

        #detecting whether their number was too high or too low
        if ran_num > user:
            print("The number is too low")
        elif ran_num < user:
            print("The number is too high")

        #breaks out of the loop if they guessed the number
        else:
            guessed = True
            break


    #same as if guessed = true
    if guessed:
        print("\nYou have guessed the number!",\
              "\nIt took you",counter,"guesses to get the number!")
    #if they did not guess the number
    else:
        print("You failed to guess the number, the number was",ran_num)

#calling main function
main()
                   
        
    
