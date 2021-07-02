#Write a program to find the factorial of a number

num=-9
fac=1

if num < 0:
    print("Factorial doesn't exist for negative numbers")

elif num == 0:
    print("Factorial of 0 is 1")

else:
   for i in range(1,num+1):
        fac=fac*i
   print(f"Factorial of {num} is {fac}")
