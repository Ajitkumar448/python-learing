import time #importing the time module to work with time-related functions
tomestamp = time.strftime("%Y-%m-%d %H:%M:%S")#it will give the current date and time in the format of year-month-day hour:minute:second
print("the current date and time is: ", tomestamp)
timestamp =int(time.strftime("%H"))#it will give the current hour in 24 hour format
print("the current hour is: ", timestamp)
timestamp = int(time.strftime("%M"))#it will give the current minute
print("the current minute is: ", timestamp)
timestamp = int(time.strftime("%S" ) )#it will give the current second
print("the current second is: ", timestamp)
if int(timestamp) < 12 and int(timestamp) >= 0:
    print("good morning")
elif int(timestamp) < 18 and int(timestamp) >= 12:
    print("good afternoon")
else:
    print("good evening")