# Write a program to find the factorial of a number using function

num=int(input('Enter the number: '))
def factorial(num):
    fac=1

    for i in range(1,num+1):
     fac=fac*i
    print(fac)

factorial(num)