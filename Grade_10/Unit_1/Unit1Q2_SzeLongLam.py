#Name: Sze Long Lam
#Date: Feb 23rd 2024
#Purpose: Performs math operations on two integers based on user input

#Asks the user for the input of two integers

Integer_one = int(input("Enter an integer: "))
Integer_two = int(input("Enter another integer: "))


#Calculating sum then outputting(extra\n to move to new line)

Sum = Integer_one + Integer_two
print("\nThe sum of these two numbers are:", Sum)


#Calculating difference then outputting using print statement

Difference = Integer_one - Integer_two
print("The difference of these two numbers are:", Difference)
                  

#Calculating product then outputting

Product = Integer_one * Integer_two
print("The product of these two numbers are:", Product)

                  
#Calculating quotient then outputting
#format and ".2f" is used to round down to the 2nd decimal

Quotient = format(float(Integer_one/Integer_two),".2f")
print("The quotient of these two numbers are:", Quotient)
                  

#Calculating the exponent then outputting
#The Exponent will always be a whole number therefore
#format and ".2f" are not needed

Exponent = float(Integer_one**Integer_two)
print(Integer_one,"to the exponent",Integer_two,"is:",Exponent)
