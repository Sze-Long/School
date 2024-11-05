#NAme: Szelong
#Purpose: Calculate running total
#Date: April 2nd

Max = 10

def main():
    total = 0.0
    #greeting
    print("Calculate sum of numbers")
    #loops 4 times
    for counter in range(Max):
        number = int(input("Enter a number:"))
        total += number
    #display total
    print("total is",total)
#call the main
main()
        
