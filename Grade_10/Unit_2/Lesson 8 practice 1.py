#Name: Sze Long Lam
#Date: March 18th
#Purpose: Award points based on the amount of books the customer purchases

#asks user to input the number of books that they purchased
books = int(input("Greeting user how many books did you purchase? "))

#creating the main function
def main():
    #using if else statements to determine statement
    if books >= 5:
        #gives points based on number of books purchased
        points = 60
    elif books == 4:
        points = 30
    elif books == 3:
        points = 15
    elif books == 2:
        points = 5
    else:
        points = 0

    #print statement back to the user
    print("You have purchased", books,"books this month and you gain",\
          points, "points.")

#calling the main function
main()
    
        

