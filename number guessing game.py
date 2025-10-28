# number guessing game
import random
# this picks number between 0 aand 10
secret = random.randint(0, 10)
while True:
    number = int(input("Guess the number between 0 and 10: "))
    difference = abs(secret-number)
    if number == secret:
        print("CORRECT ANSWER!!!!🎉🎉")
        break
    elif difference <= 2:
        print("YOU ARE VERY CLOSE!!!!")
    elif difference >= 5:
        print("HIGH OR LOW")
    else:
        print("KEEP TRYING AGAIN")
