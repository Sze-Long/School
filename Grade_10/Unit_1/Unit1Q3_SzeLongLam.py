#Name: Sze Long Lam
#Date: Feb 23rd 2024
#Purpose: Outputs a greeting based on the input the user gave

#Asks the user for their name,money saved per month, and current year

Name = input("What is your name? ")
Money_per_month = float(input("How much money do you save per month? "))
Current_year = int(input("What is the current year? "))

#format and ".2f" is used to round down to the 2nd decimal
#Rounding down because we need to perform some operations

Money_per_month = float(format(Money_per_month, ".2f"))

#calculating money in 10,20 and 30 years
#this will make it be rounded to the tenth decimal place

Ten_years = Money_per_month * 120
Twenty_years = Money_per_month * 240
Thirty_years = Money_per_month * 360


#printing out the greeting for the user
print("Hello, ", Name,"!",sep = "")
print("In 10 years, you will get $", Ten_years,\
      "In 20 years, you will get $", Twenty_years,\
      "In 30 years, you will get $", Thirty_years,".")

#Asks the user to input X amount of years

Future_Years = int(input("In how many years do you\
 wish to know the money you have? "))

Total_money = Money_per_month * Future_Years * 12

print("In", Future_Years,"years, you will get $", Total_money)




