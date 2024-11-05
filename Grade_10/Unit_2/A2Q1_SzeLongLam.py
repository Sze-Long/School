#Name: Sze Long Lam
#Date: March 21st 2024
#Purpose:Calculates and displays a person's body mass index

#global variables for kg and meters
#1 kg in terms of pounds
kg_1 = 2.20462
#1 inch in tersm of meters
in_1 = 0.0254

#defining the main fuction
def main():

    #asks the user to enter their height in pounds and height in inches
    user_in_height = float(input("What is your height = "))
    user_po_weight = float(input("What is your weight = "))
    #adds a new line
    print("")

    #Changes weight from pounds to kg
    user_kg_weight = user_po_weight/kg_1
    #Changes height from inches to cm
    user_m_height = user_in_height*in_1

    #processing the total BMI using height and weight
    BMI = float(format(user_kg_weight/(user_m_height**2),".2f"))

    #if and else statements to determing whether the user is
    #obese normal or normal weight
    if BMI >= 25.0 and BMI <=29.9:
        #user is overweight and not underweight
        print("According to BMI CLassifications, Your BMI is",BMI,\
              "and you are overweight. Please consider exercising for"\
              ,"prolonging your longevity. You have an increase in risk"\
              ,"for developing health problems. You can do it!")
    
    elif BMI <= 24.9 and BMI >= 18.5:
        #user is not overweight or underweight
        print("According to BMI CLassifications, Your BMI is",BMI,\
              "and you are normal weight. Please consider walking everyday for"\
              ,"prolonging your longevity. You can do it!")
    elif BMI < 18.5:
        #user is underweight and not overweight
        print("According to BMI CLassifications, Your BMI is",BMI,\
              "and you are underweight. Please consider eating more for"\
              ,"prolonging your longevity. You have an increase in risk"\
              ,"for developing health problems. You can do it!")
    else:
        #user is really overweight
        print("According to BMI CLassifications, Your BMI is",BMI,\
              "and you are obese. Please consider exercising for"\
              ,"prolonging your longevity. You have an increase in risk"\
              ,"for developing health problems. You can do it!")
        
#calling the main function 
main()
    
