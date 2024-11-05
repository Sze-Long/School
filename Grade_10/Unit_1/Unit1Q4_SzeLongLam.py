#Name: Sze Long Lam
#Date: Feb 23rd 2024
#Purpose: Calculates the volume of a sphere based on the radius

#Asks the user for the radius of the sphere

Radius = float(input("Enter the radius= "))
Pi = 3.14

#performing operations to find volume and area

Volume = 4/3 * Pi * Radius**3
Area = 4 * Pi * Radius**2

#Outputting these numbers

print("The volume of the sphere is approximately", Volume,\
      "cm.The area of a sphere is approximately", Area,"cm squared.")

#This is Part B of the question

print("\n")#This just adds two lines

#performing operations to find volume and area
#format and ".2f" is used to round down to the 2nd decimal

Rounded_Volume = format(4/3 * Pi * Radius**3,".1f")
Rounded_Area = format(4 * Pi * Radius**2,".1f")

#Outputting these numbers

print("The volume of the sphere is approximately", Rounded_Volume,\
      "cm.The area of a sphere is approximately", Rounded_Area,"cm squared.")



