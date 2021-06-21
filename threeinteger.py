#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1=int(input('Enter the value:'))
num2=int(input('Enter the value:'))
num3=int(input('Enter the value:'))

if num1==num2 or num2==num3 or num1==num3:
  sum=0

else:
 sum=num1+num2+num3


print(sum)