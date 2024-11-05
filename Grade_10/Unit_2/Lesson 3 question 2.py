#Name: Sze Long
#Date: March 4th 
#Purpose: Planning a roadtrip

def trip_statistics(destination,start_point,distance,travel_time):
    #average speed is distance over travel time
    average_speed = distance/travel_time

    thelist = [distance,average_speed]
    print("You are traveling from",destination,"to",start_point,\
          "The total distance is", distance,"and the average speed is",\
          average_speed)


trip_statistics('Beach City', 'Home Town', 250,5 )
