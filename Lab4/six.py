#Write a Python program to count the number of even and odd numbers from a series of numbers.

num=(1,2,3,4,5,6,7,8,9)
even=0
odd=0
for i in num:
  if  i%2 == 0:
      even+=1


  else:
      odd+=1
print("The number of odd numbers:",odd)
print("The number of even numbers:",even)