#Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def check(num):
  counter =0
  for i in range(1,num+1):
    if num % i ==0:
      counter = counter +1

  if counter ==2 :
    print('Its a prime number')

  else:
    print('It is not a prime number')


check(7)



