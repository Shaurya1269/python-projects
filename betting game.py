import random

balance = 1000

print("Welcome to the betting game!")
while balance > 0:#put indetation after this for each line,otherwise it wont work 
    secret = random.randint(1, 32)
    print("Your starting balance is: ", balance)

    bet_amount = int(input("Enter your bet amount: "))
    balance = balance-bet_amount
    print("Your current balance is: ", balance)
    user_input = int(
    input("Enter a number between 1 and 32 on which you want to bet on: "))


    if bet_amount > balance:
        print("Insufficient balance.")
        continue 
        
        
    no_of_tries = 3
    if user_input == secret:
        print("congratulations! You win!")
        balance = balance + bet_amount*2
        print("Your new balance is:", balance)
        no_of_tries = 3
        print("You still have", no_of_tries, "tries left")

    while no_of_tries > 1:
        no_of_tries -= 1
        print("Sorry,try again!,you still have", no_of_tries, "tries left")
        user_input = int(
        input("Enter a number between 1 and 32 on which you want to bet on: "))
        if no_of_tries == 1 and user_input != secret:
            print("Sorry, you have no tries left. The correct number was", secret)

            print("Your balance is: ", balance)
        if user_input == secret:
            print("congratulations! You win!")
            balance = balance + bet_amount*2
            print("Your new balance is:", balance)




