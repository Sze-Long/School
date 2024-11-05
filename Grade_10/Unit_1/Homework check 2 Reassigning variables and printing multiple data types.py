#Name: Sze Long Lam
#Date: February 9th
#Program Purpose: reasigning variables and print function with multiple pieces of data

Base = int(input("Input a positive integer "))
#printing the current base and telling the user that we are adding it by 5
print("the number you input is", str(Base)+ ". We will now add 5")
#I turned Base into a string so that I could take out the space before the period)
#adding 5 to the base
Base += 5

print("After adding 5 the number is", str(Base)+ ". We will now multiply by 5") #same as last time
#multiplying 5 to the base
Base = Base * 5

print("After multipliying 5 the number is", str(Base)+ ". We will now subtract by 5") #same as last time
#subtracting 5 to the base
Base -= 5

print("After subtract 5 the number is", str(Base)+ ". We will now divide by 5") #same as last time
#dividing by 5 then rounding it to the nearest integer
Base = int(Base/5)

print("After dividing 5 the number is", str(Base)+ ".", "Your final number is", str(Base)+ ".") #same as last time
