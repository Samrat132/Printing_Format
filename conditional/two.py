'''
 If temperature is greater than 30, it's a hot day other wise if it's less than 10;
 it's a cold day; otherwise, it's neither hot nor cold.
'''
temper = int(input("Enter the value of tempreature:"))

if temper >30:
    print("Its a hot day")
elif temper <10:
    print("Its a cold day")
else:
    print("Its neither hot nor cold")