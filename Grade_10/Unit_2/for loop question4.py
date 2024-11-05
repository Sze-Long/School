#Name: Sze Long Lam, Curtis
#Date: 28th March 2024
#Purpose: rabbit calculation

#stating the global variables
initial_rabbit = 100
months = 12

#main function
def main():
    #greeting
    print("Your rabbit calculations")
    #header of the table
    print("month\t|\tcurrent rabbits")
    #the loop for the numbers
    for current_month in range(1,months+1):
        #calculating the number of current rabbits
        current_rabbit = initial_rabbit * 2**(current_month-1)
        #outputing the results back to the user
        print(current_month,"\t|\t",current_rabbit,sep = "")

#calling the main function
main()

