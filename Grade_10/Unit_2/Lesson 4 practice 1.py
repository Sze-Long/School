#Name: SzeLong Lam
#Purpose: calulates chris's pay
#Date: March 5th

def main():
    #asks user to input hours work and hourly pay
    hours = int(input("How many hours worked?"))
    #rounds to second decimal and makes it a float
    pay_hour = float(format(float(input("What is pay?")),".2f"))
    if hours >= 40:
        #formula to get total pay
        Total_pay = 40*pay_hour + float(format((hours-40)*pay_hour*1.5))
        
    else:
        #total pay if less than 40 hours
        Total_pay = hours*pay_hour

    print("Your pay is",Total_pay)

main()
