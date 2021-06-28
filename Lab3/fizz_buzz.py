#Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

def fizz_buzz():
    for fizz_buzz in range (50):
        if fizz_buzz %3 ==0 and fizz_buzz % 5 ==0 :
            print("FizzBuzz")
            return

        elif fizz_buzz % 5 ==0:
          print("Buzz")
          return

        elif fizz_buzz % 3 ==0 :
            print("Fizz")
            return


fizz_buzz()

