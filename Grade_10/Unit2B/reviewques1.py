#Name: Sze Long
#Date: April 10th 2024
#Purpose: Geometry Calculator

def main():
    #greeting and explanation of the code
    print("Geometry Calculator Menu:\n1. Calculate area of square\n2."\
          ,"Calculate perimeter of square\n3.Calculate area of rhombus\n4."\
          ,"Calculate perimeter of rhombus\n5.Exit\n")
    #allows the user to choose one of the 5 choices
    user = input("Enter your choise (1-5): ")
    
    #if the user chose to exit
    if user == "5":
        print("Exiting the program")
    #only the area of rhombus needs height and base
    elif user == "3":
        height = int(input("Enter height of rhombus"))
        base = int(input("Enter base of rhombus"))
        print("The area of the rhombus is",formulas.arhombus(height,base))
        
    #all the others only need one side of the shape
    else:
        side_length = int(input("Enter sidelength of shape"))
        #if the user picked area of the square
        if user == "1":
            print("The area of the square is",formulas.asquare(side_length))
        #user picked perimeter of square
        elif user == "2":
            print("The perimeter of the square is",formulas.perimeter(side_length))
        #user picked perimeter of rhombus (option 4)
        else:
            print("The perimeter of the rhombus is",formulas.perimeter(side_length))

