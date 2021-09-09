import random
EASY_LEVEL_LIFE=10
TOUGH_LEVEL_LIFE=5
print("Let's play NUMBER GUESSING game between 1-100")
while(True):
    level=input("You want to play tough level or easy level game?").lower()
    if level=='easy':
        life = EASY_LEVEL_LIFE
        randomnumber = random.randint(1, 100)
        while(True):


            guess=int(input("Enter your guess:  "))
            if(guess>randomnumber):
                print("Too large ")
                life=life-1
                print("Life remaining is",life)
                if(life==0):
                    print("You loose!!")
                    break
            elif(guess<randomnumber):
                print("Too low")
                life=life-1
                print("Life remaining is", life)
                if (life == 0):
                    print("You loose!!")
                    break
            else:
                print("You guessed it right!! You won ")
                break
    elif level=='tough':
        life = TOUGH_LEVEL_LIFE
        randomnumber = random.randint(1, 100)
        while(True):


            guess=int(input("Enter your guess:  "))
            if(guess>randomnumber):
                print("Too large ")
                life=life-1
                print("Life remaining is",life)
                if(life==0):
                    print("You loose!!")
                    break
            elif(guess<randomnumber):
                print("Too low")
                life=life-1
                print("Life remaining is", life)
                if (life == 0):
                    print("You loose!!")
                    break
            else:
                print("You guessed it right!! You won ")
                break
    else:
        print("You can't see the question !!")
        continue

    continueagain=input("Enter Y to play again ,N to exit game").lower()
    if(continueagain=='n'):
        break


