#Name: Sze Long Lam
#Purpose: Practice data output
#Date: February 20th, 2024

#input hours per month
hours = float(input("hours per month"))
#input hourly wage
wage = float(input("hourly wage"))
#calculate hours per year
yearly = format(hours*wage*12,".2f")
#prints out yearly amount
print("You made $",yearly,"every year")
#calculates with salary bonus
bonus = float(yearly)
bonus1 = format((bonus*1.05),".2f")
#prints out with bonus
print("With bonus, Annual salary is", bonus1)
