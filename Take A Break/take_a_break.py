
#This is a program which you can use to plan your study routine while studying

import webbrowser
import time

break_count=0
interval=3 #Change the value of interval to increase or decrease the number of your study intervals

print ("This program started on: "+time.ctime())

while break_count<interval: 
    time.sleep(1800) #Change the number inside this sleep function to increase or decrease the time of your 1 study interval
    webbrowser.open("https://www.youtube.com/watch?v=9qUzY0Hv4GY")  
    break_count+=1
    print break_count
