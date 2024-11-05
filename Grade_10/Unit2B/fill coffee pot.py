#name: Sze Long
#Date: April 3rd 2024
#Purpose: How long to fill a coffee pot

day = 0.0
coffee_pot = 10.0
def main():
    print("Welcome to this program, this program will tell you how long it"\
          ,"takes to fill a coffee pit")
    total = 0.0
    coffee_not_filled = True
    while coffee_not_filled:
        fill = input("enter filling amount in L?")
        total += fill
        if total >= coffee_pot:
            print("you have filled the coffee pot")
            coffee_not_filled = False
        else:
            print("coffee pot is not filled yet")
            
        
