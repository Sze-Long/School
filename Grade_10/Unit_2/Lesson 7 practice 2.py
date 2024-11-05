#Name: Sze Long
#Purpose: Managing vip book club
#Date: March 8th

part_of_libary = 2
overdue_fines = 0

def main()
    print("You need to be in the libary for 2 years, have no overdue fines",\
          "and agree to the terms and conditions") #greeting
    #user inputs years fines and agreement
    libary_years = int(input("How long were you a part of the libary"))
    user_fines = int(input("How many fines do you have"))
    agreement = int(input("Do you agree to join the club(with yes or no",\
                          "no capitals"))
    
    if libary_years >= part_of_libary and user_fines == overdue_fines and
    agreement == yes
        
    else:
        print("You don't meet all the requirements")
    
main()
