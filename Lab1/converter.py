import random
randomnum=random.randint(1,8)
attempt_left =3
while attempt_left >0:
    attempt_left -=1
    guess = int(input('Enter the number again:'))
    if guess == randomnum:
        print('Congrates! You guess it right.')
        break
else:
    print("No attempts left")



