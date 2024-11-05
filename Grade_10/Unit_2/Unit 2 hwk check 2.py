#name: Szelong
#date: March 8th
#Purpose: acceptance to after school program

#variables for the maximum and minimum age
maximum_age = 18
minimum_age = 12

def main()
    #greeting statement
    print("We are now accepting members to our afterschool program")

    #asks the user for their age
    age = input("How old are you?")

    #if their age falls into the age gap
    if age <= maximum_age and age >= minimum_age:
        print("You are eligible for the afterschool program")

    #if their age does not fall into the age gap
    else:
        print("You are not eligible for the afterschool program")
        
main()#calling the main function
