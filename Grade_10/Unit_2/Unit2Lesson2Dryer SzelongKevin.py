#Name: Sze Long, Kevin
#Date: Feb 28th
#Purpose: Create a dishwasher dismantler

#creates main function

def main():
    move_dryer()
    remove_screws()
    remove_back_panel()
    pull_top()
    
#steps for moving the dryer
def move_dryer():
    input("Unplug dryer from wall")
    input("Move dryer from wall")
    
#steps for removing screws
def remove_screws():
    input("Remove the six screws from dryer")

#step for removing back panel
def remove_back_panel():
    input("Remove the back panel")

#steps for removing the top
def pull_top():
    input("Pull top from dryer")
    

#calling the main function
main()
