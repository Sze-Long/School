#Name: Sze Long Lam
#Date: March 21st 2024
#Purpose:  Change counting game

#global variables which are always true
nickel = 0.05
dime = 0.10
quarter = 0.25
dollar = 1.00

#defining the main function
def main():
    #greeting
    print("Hello, Jane!\n")
    
    #user inputing nickel, dime and quarters
    num_nickel = int(input("Enter number of nickel "))
    num_dime = int(input("Enter number of dime "))
    num_quarter = int(input("Enter number of quarter "))

    #calculating the total price of these three coins seperately
    total_nickel_price = float(format(num_nickel * nickel,".2f"))
    total_dime_price = float(format(num_dime * dime,".2f"))
    total_quarter_price = float(format(num_quarter * quarter,".2f"))

    #adding all of those together    
    total_price = total_nickel_price + total_dime_price + total_quarter_price

    #if statements to determing whether is it a dollar and determine
    #the difference if there is any
    if total_price == dollar:
        Equal_dollar = True
        difference = 0
    elif total_price >= dollar:
        Equal_dollar = False
        difference = format(total_price - dollar,".2f")
    else:
        #not more or equal to dollar so its less
        Equal_dollar = False
        difference = format(dollar - total_price,".2f")

    #print statements back to the user
    #regarding the number of coins entered
    print("\nnumber of nickel entered: ",num_nickel)
    print("number of dime entered: ",num_dime)
    print("number of quarter entered: ",num_quarter,"\n")

    #exactly how I made the calculations
    print(num_nickel," nickel(s) - ",num_nickel," * ",nickel," = ",\
          total_nickel_price,sep="")
    print(num_dime," dime(s) - ",num_dime," * ",dime," = ",\
          total_dime_price,sep="")
    print(num_quarter," quarter(s) - ",num_quarter," * ",quarter," = ",\
          total_quarter_price,sep="")

    #regarding the total price of each coin
    print("you have entered $",total_nickel_price,"of nickels")
    print("you have entered $",total_dime_price,"of dime")
    print("you have entered $",total_quarter_price,"of quarter\n")

    #different answer if they got it correct or wrong
    if Equal_dollar:
        print("You have entered coins equal to a dollar")
    else:
        print("Unfortunatly your difference is",difference)

#calling main function
main()

    
        
    
