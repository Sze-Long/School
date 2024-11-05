#Name: Sze Long
#Date: March 5th
#Purpose:Detective problem

Angel = "I was at the library studying for my exams all evening."
Devil = "I was at the gym working out until late."
Chimera = "I was at home watching movies with my family."

def find_culprit(angel_statement,devil_statement,chimera_statement):
    #Whichever has the longest sentence is guilty
    #checking if angel's statement is longer
    if len(angel_statement) > len(devil_statement) and \
       len(angel_statement) > len(chimera_statement):
        print("Angel is guilty")
    #checking if devil's statement is longer
    elif len(devil_statement) > len(angel_statement) and \
       len(devil_statement) > len(chimera_statement):
        print("Devil is guilty")
    #checking if chimera's statement is longer
    elif len(chimera_statement) > len(devil_statement) and \
       len(chimera_statement) > len(angel_statement):
        print("chimera is guilty")
    else:
        print("They are all guilty")


find_culprit(Angel,Devil,Chimera)
    
