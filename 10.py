#Write a Python program to convert seconds to day, hour, minutes and seconds.

sec = int(input('enter the time in sec:'))
day = (((sec//60)//60)//24)
print (f"Total day for given sec is {day} days")

hour = ((sec//60)//60)
print(f"Total hours for given sec is {hour} hours")

min=(sec//60)
print(f"Total min for given sec is {min} mins")

sec=sec
print(f"Total sec for given sec is {sec} secs")
