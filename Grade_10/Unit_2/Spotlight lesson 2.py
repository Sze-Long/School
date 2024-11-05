#Name: Sze Long
#Date: March 4th
#Purpose: practicing functions

def questions()
    #introduction to the user
    input("hello I will be deducting 5% from your pay and bonus")

    #asks the user for their pay and bonus
    gross_pay = float(input("What is your gross pay"))
    bonus = float(input("What is your bonus"))
    calculate(gross_pay,bonus)
def calculate(gross_pay,bonus)
    deducted_pay = format(gross_pay * 0.95,".2f")
    deducted_bous = format(bonus * 0.95,".2f")
    print("your gross pay after deduction is", deducted_pay)
    print("your gross bouns after deduction is", deducted_bonus)

questions()
