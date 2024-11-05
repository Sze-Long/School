#Name: Sze Long Lam
#Date: Feb 23rd 2024
#Purpose: Calculate total revenue for BOSS Drama Final Performance

#Asks user for the cost of student and parent seats

Student_cost = float(input("Enter cost for student seats: "))
Parent_cost = float(input("Enter cost for parent seats: "))

#Asks user for the number of students and parents
#The backslash n is for skipping a line

Student_number = int(input("\nThe number of students = "))
Parent_number = int(input("The number of parents = "))

#Calculating the profits of the sales if the house is full
#Total cost is the Student cost times Student number 
#and the Parent cost times the Parent number
#format and ".2f" is used to round to the nearest 2nd decimal

Student_profit = format((Student_cost * Student_number),".2f") 
Parent_profit = format((Parent_cost * Parent_number),".2f")

Total_profit = float(Student_profit) + float(Parent_profit)


#Outputting the profit of the sales

print("The profit of the sales if full house is: $",Total_profit,sep="")


