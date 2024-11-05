#Name: Sze Long Lam
#Date: March 6th
#Purpose: Determine the larger of two numbers

def main():
    #asks the user for two numbers to input
    num1 = float(input("Input first number: "))
    num2 = float(input("Input second number: "))

    #compares the two numbers and sees which one is larger
    if num1 > num2:
        print(num1,"is greater than", num2)

    #elif statement to figure out if num2 is larger or is equal to num1
    elif num2 > num1:
        print(num2,"is greater than", num1)

    #if one is not larger than the other they are both equal
    else:
        print("They are both equal")

#calling the main function
main()
