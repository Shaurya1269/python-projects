# number guessing game but more advanced or easy
import random
# this picks number between 0 aand 100
secret = random.randint(0, 100)
# this while True expression i used for the loop to work infinitely till u get desired result
while True:
    number = int(input("Guess the number between 0 and 10: "))
    difference = (secret-number)
    if number == secret:
        print("CORRECT ANSWER!!!!🎉🎉")
        break
    elif difference <= 5:
        print("YOU ARE VERY VERY CLOSE!!!!....JUST CHOOSE A HIGHER NUMBER")
    elif difference >= 10:
        print("YOU ARE CLOSE...JUST CHOOSE A HIGHER NUMBER")
    elif difference <= -5
    print("YOU ARE VERY VERY CLOSE...JUST CHOOSE A SMALLER NUMBER")
    elif difference >= -10
    print("YOU ARE CLOSE....JUST COHOSE A SMALLER NUMBER")
    else:
        print("KEEP TRYING AGAIN")
