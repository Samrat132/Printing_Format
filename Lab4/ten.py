# Write a Python program that accepts a string and calculate the number of digits and letters


str =input('Enter the string :')
dig=lett=0

for i in str:
    if i.isdigit():
        dig+=1


    elif i.isalpha():
        lett+=1
print(f"Letters : {lett}")
print(f"Digits : {dig}")

