#Name: Sze Long Lam
#Date: February 8th - 9th
#Program purpose: Prints out an information sheet based on given information
#Program second purpose: Learn more about variable reasignment

#str meaning we turn it into a string 
name = str(input("What is your name? ")) #ask user for name and stores it in variable
#int meaning we turn it into an integer (if not then it rounds)
age = int(input("What is your age? ")) #ask user for age and stores it in variable

if name == "SzeLong" and age == 15: #checks whether it is SzeLong
    height = 150 #If it is then we know all other information
    date_of_birth = "13th March 2008"
    fav_colour = "Orange"
    dream_car = "Electric_Mazda"
    fav_game_genre = "Tower Defence"

else: #If we don't then all others have to be typed manualy
    height = str(input("How tall are you?(in cm) "))
    date_of_birth = str(input("When are you born? "))
    fav_colour = str(input("What is your favourite colour? "))
    dream_car = str(input("What is your dream car? "))
    fav_game_genre = str(input("What is your favourite game genre? "))

print("Your name is ", name); #Prints name
if age <= 17: #if age is less than 17 then you can still graduate highschool)
    print("you will graduate highschool in", 17 - age, "years");
if age <= 20: 
    print("you will stop using this computer in", 21 - age, "years");

print("You are", height, "cm tall\nYour Birthday is", date_of_birth, "\nYour favourite colour is"
      , fav_colour,"\nYour dream car is", dream_car, "\nYour favourite game genre is", fav_game_genre, "\n");

#changing the variable
height += 5
fav_colour = "Green"
dream_car = "Lambo"
fav_game_genre = "Adventure"
age += 2
print("In two years, Your name is ", name); #Prints name with 2 years more
if age <= 17: #if age is less than 17 then you can still graduate highschool)
    print("you will graduate highschool in", 17 - age, "years");
if age <= 20: 
    print("you will stop using this computer in", 21 - age, "years");
print("You are", height, "cm tall\nYour Birthday is", date_of_birth, "\nYour favourite colour is"
      , fav_colour,"\nYour dream car is", dream_car, "\nYour favourite game genre is", fav_game_genre);


    
