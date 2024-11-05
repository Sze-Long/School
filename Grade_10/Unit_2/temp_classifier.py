#Name: Mariam & Kelly
#Date: 27th February 2024
#Purpose: Temp classifier


#defining the main function
def main():
    #greeting
    print("This program classifies temprature")
    while True:
        #ask the user for the temprature
        temperature = float(input("what is the temprature?"))
        
        #if statements to determine output back to user
        if temperature <= 0:
            print("freezing")
        elif temperature >0 and temperature <=10:
            print("cold")
        elif temperature >10 and temperature <=20:
            print("cool")
        elif temperature >20 and temperature <=30:
            print("warm")
        else:
            print("hot")
#calling the main function
main()
