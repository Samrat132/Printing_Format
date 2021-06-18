'''
game finding a secret number within 3 attempts using while loop
'''
import random
randomnum=random.randint(1,8)
attempt=2
while attempt >=0:
    guess = int(input('Enter the number again:'))
    if guess == randomnum:
        print('Congrates! You guess it right.')
        break
    else:
      print(f"{attempt} attempt left")
      attempt=attempt-1