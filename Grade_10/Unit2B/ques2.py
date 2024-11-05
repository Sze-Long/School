#Name: Sze Long Lam
#Date: April 11th 2024
#Purpose: Calculate area or perimeter of shapes

#importing my formulas into this program
import szeformula

def main():
    #Greeting
    print("Welcome this program will calculate the area and perimeter of",\
          "a triangle and trapezoid\n")
    while True:
        #explaining how the program will work
        print("Geometry Calculator Menu:\n1. Calculate the area of a triangle",\
              "\n2. Calculate the perimeter of the triangle\n3. Calculate the",\
              "area of a trapezoid\n4. Calculate the perimeterof a trapezoid",\
              "\n5. Exit")
        #user input value from 1-5
        user = int(input("Enter your choice from 1-5: "))
        #if the users number is not from 1-5
        while user >= 6 and user <= 0:
            print("Enter a valid number from 1-5")
            user = int(input("Enter your choice from 1-5: "))

        #area of triangle
        if user == 1:
            base = int(input("Enter base of triangle"))
            #validation loop for base
            while base <= 0:
                print("Enter a number larger than 0")
                base = int(input("Enter base of triangle"))
                
            height = int(input("Enter height of triangle"))
            #validation loop for height
            while height <= 0:
                print("Enter a number larger than 0")
                height = int(input("Enter height of triangle"))
            print("The area of the triangle is",\
                  szeformula.area_triangle(base,height),"\n")

        #perimeter of triangle
        elif user == 2:
            #side 1
            side_1 = int(input("Enter first side of triangle"))
            while side_1 <= 0:
                print("Enter a number larger than 0")
                side_1 = int(input("Enter first side of triangle"))

            #side 2
            side_2 = int(input("Enter second side of triangle"))
            while side_2 <= 0:
                print("Enter a number larger than 0")
                side_2 = int(input("Enter second side of triangle"))

            #side 3
            side_3 = int(input("Enter third side of triangle"))
            while side_3 <= 0:
                print("Enter a number larger than 0")
                side_3 = int(input("Enter third side of triangle"))

            print("The perimeter of the triangle is",\
                  szeformula.perimeter_triangle(side_1,side_2,side_3),"\n")

        #area of trapezoid
        elif user == 3:
            base = int(input("Enter base of trapezoid"))
            #validation loop for base
            while base <= 0:
                print("Enter a number larger than 0")
                base = int(input("Enter base of trapezoid"))

            oppbase = int(input("Enter oppisite side of base of trapezoid"))
            #validation loop for oppbase
            while oppbase <= 0:
                print("Enter a number larger than 0")
                oppbase = int(input("Enter oppisite side of base of trapezoid"))
                
            height = int(input("Enter height of trapezoid"))
            #validation loop for height
            while height <= 0:
                print("Enter a number larger than 0")
                height = int(input("Enter height of tra[ezpod"))
            print("The area of the triangle is",\
                  szeformula.area_trapezoid(base,height,oppbase),"\n")

        #perimeter of trapezoide
        elif user == 4:
            #side 1
            side_1 = int(input("Enter first side of trapezoid"))
            while side_1 <= 0:
                print("Enter a number larger than 0")
                side_1 = int(input("Enter first side of trapezoid"))

            #side 2
            side_2 = int(input("Enter second side of trapezoid"))
            while side_2 <= 0:
                print("Enter a number larger than 0")
                side_2 = int(input("Enter second side of trapezoid"))

            #side 3
            side_3 = int(input("Enter third side of trapezoid"))
            while side_3 <= 0:
                print("Enter a number larger than 0")
                side_3 = int(input("Enter third side of trapezoid"))

            #side 4
            side_4 = int(input("Enter fourth side of trapezoid"))
            while side_4 <= 0:
                print("Enter a number larger than 0")
                side_4 = int(input("Enter fourth side of trapezoid"))

            print("The perimeter of the trapezoid is",\
                  szeformula.perimeter_trapezoid(side_1,side_2,side_3,side_4),\
                  "\n")

        #user chose to exit
        else:
            print("Ending loop")
            break

#You will need to type in the first line: import ques2
#On the second line you will need to type: ques2.main()
#Then the program will start
