#Name: Sze Long Lam
#Date: March 21st 2024
#Purpose: calculate total price for paint job

#global variables for labor 20 dollars per hour
labor_hour = 20.00
def main():
    #asks user to input square feet and price per gallon
    sq_feet = float(input("What is the square feet of the wall to be painted"))
    price_gallon = float(input("What is the price of paint per gallon needed"))

    #formula for total gallons
    total_gallon = float(format(sq_feet / 115,".2f"))
    #formula for total hours of labor
    hours_labor = float(format(sq_feet / 115 * 8,".2f"))
    #formula for cost of paint
    cost_paint = float(format(total_gallon * price_gallon,".2f"))
    #formuma for cost of labor
    cost_labor = float(format(hours_labor * labor_hour,".2f"))
    #formula for total cost
    total_cost = float(format(cost_paint + cost_labor,".2f"))
    #ouputing the results in seperate function
    output(sq_feet,total_gallon,hours_labor,cost_paint,cost_labor,total_cost)

def output(sq_feet,total_gallon,hours_labor,cost_paint,cost_labor,total_cost):

    #print statements back towards the user
    print("for",sq_feet,"square feet of wall space, you will need:")
    print(total_gallon,"gallons of paint")
    print(hours_labor,"total ammount of labor")
    print(cost_paint,"total cost of paint")
    print(cost_labor,"total cost of labor")
    print("total cost of paint job is",total_cost)

#calling main function
main()

    
                    
