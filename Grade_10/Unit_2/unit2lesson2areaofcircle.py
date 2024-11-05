#Name: Sze Long Lam,Kevin
#Date: Feb 28th
#Purpose: Calculates the area of a circle

#making a variable called pi
Pi = 3.14159

def main():

    #setting radius to global
    global radius
    
    #asking the user for data
    radius = float(input("What is the radius"))

    #calls the function circle area
    calculate_circle_area()

def calculate_circle_area():
    print(Pi*radius**2)
    

main()
