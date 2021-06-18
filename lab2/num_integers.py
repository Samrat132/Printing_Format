#Given three integers, print the smallest one.
# (Three integers should be user input)

num1= int(input('Enter the integer_1:'))
num2= int(input('Enter the integer_2:'))
num3= int(input('Enter the integer_3:'))

if (num1<=num2 and num1<=num3):
    print(num1,"is the smallest one")

elif(num2<=num1 and num2<=num3):
    print(num2,"is the smallest one")

else:
    print(num3,"is the smallest one")