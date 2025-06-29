from playsound3 import playsound
import time


# playsound("alarm.mp3")  
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H" 

def alarm(seconds) :
    timeelasped = 0
    print(CLEAR)  
    while timeelasped < seconds :# 0<10
        time.sleep(1) # sleep for 1 second
        timeelasped += 1 #1
        time_left=seconds-timeelasped  #10-1=9
        minutes_left = time_left // 60 #9/60=0
        seconds_left = time_left % 60    #9%60=9

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")

minutes = int(input("enter the minutes to set the alarm: "))
seconds = int(input("enter the seconds to set the alarm:"))
total_seconds =minutes*60 +seconds

alarm(total_seconds)
 
