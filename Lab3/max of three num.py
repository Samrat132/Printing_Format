# Write a Python function to find the Max of three numbers

num1= input('Enter the first num:')
num2= input('Enter the second num:')
num3= input('Enter the third num:')

def num():
    if (num1>=num2) and (num1>=num3):
        max=num1

    elif (num2>=num1) and (num2>=num3):
        max=num2

    else:
        max=num3

    print(f"The max of three numbers is {max}")

num()