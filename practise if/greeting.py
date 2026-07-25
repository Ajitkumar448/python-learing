import time #importing the time module to work with time-related functions
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")#it will give the current date and time in the format of year-month-day hour:minute:second
print("the current date and time is: ", timestamp)
timestamphour =int(time.strftime("%H"))#it will give the current hour in 24 hour format
print("the current hour is: ", timestamphour)
timestampmin = int(time.strftime("%M"))#it will give the current minute
print("the current minute is: ", timestampmin)
timestampsec = int(time.strftime("%S" ) )#it will give the current second
print("the current second is: ", timestampsec)
if int(timestamphour) < 12 and int(timestamphour) >= 0:
    print("good morning")
elif int(timestamphour) < 18 and int(timestamphour) >= 12:
    print("good afternoon")
else:
    print("good evening")