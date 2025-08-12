import random

score = 10
randomNumber = random.randint(1,10)

while True:
    userNumberInput = int(input('guess : ' ))
    if( userNumberInput == randomNumber):
        print('you guess right : ' + str(score))
        break
    else:
        print("opps ! wrong guess")