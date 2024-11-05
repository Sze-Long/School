#Name: Sze Long Lam
#Date: Feb 7
#Program Purpose Understanding more about strings
Name = str(input("What is your name? "))
#User input on the name (Has to be a string)
X = str(input("Are you at Bur Oak? (Write Yes or No) "))
#User input if the answer to Are you at Bur Oak? is Yes then the location is 933 Bur Oak Ave and Postal is L6E 1G4
#If the answer is not Yes then type in the location and postal manualy
if X == "Yes":
    Location = "933 Bur Oak Ave"
    Postal = "L6E 1G4"
else:
    Location = str(input("What is your location? "))
    Postal = str(input("What is your Postal code? "))
         
#Prints out Name, Location and Postal Code
print("My name is: ", Name);
print("You are at: ", Location);
print("Your postal code is: ", Postal);
                     
