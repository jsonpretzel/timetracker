# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:09:30 2020

@author: Owner
"""
import datetime
from time import time, ctime

#setup text variables
exit = ""
stopwatch = ""
task = ""
message = "type 'exit' to close the program, or enter any key to start again: " 
unpause = ""
timeSoFar = datetime.datetime.now()- datetime.datetime.now()

 
#function to calculate the elapsed time between starting and stopping
def elapsed(start):
    current = datetime.datetime.now()
    elapse = current - start
    return elapse

#loop is True until exit command is executed to break loop
while True:
    timeSoFar = datetime.datetime.now()- datetime.datetime.now()

    task = input("Enter the name of the task you are tracking: ")
    while (stopwatch != "s"):
        stopwatch = input("Enter s to begin:")
    
    start = datetime.datetime.now()

    while(stopwatch != "x"):
        stopwatch = input("Enter p to pause or x to stop: ")
        
        if stopwatch == "p":
            timeSoFar += elapsed(start)
            while unpause != 'p':
                print(f"Time elapsed so far: {timeSoFar}")
                unpause = input("Enter 'p' to unpause: ")
            start = datetime.datetime.now()
            stopwatch = ""
            unpause = ""
            
#if enter "s", start stopwatch
#   display elapsed time every 30 seconds
#if enter "s" again, stop stopwatch
#   display total elapsed time 
    total = elapsed(start) + timeSoFar
    print(f"Total time spent on {task}:", total) 
    exit = input(message)
        
    if exit == "exit":
        break
    else:
        task = ""
        continue
