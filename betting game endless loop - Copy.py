import random

balance = 1000
print("Welcome to the betting game!")
print("Your starting balance is:", balance)

while balance > 0:
    print("\nYour current balance is:", balance)

    bet_amount = int(input("Enter your bet amount: "))
    if bet_amount > balance:
        print("Insufficient balance! Try again.")
        continue

    balance -= bet_amount  # Deduct bet after validation
    secret = random.randint(1, 32)
    no_of_tries = 3

    while no_of_tries > 0:
        user_input = int(input("Enter a number between 1 and 32: "))

        if user_input == secret:
            print("🎉 Congratulations! You win!")
            balance += bet_amount * 2  # Win amount
            break
        else:
            no_of_tries -= 1
            if no_of_tries > 0:
                print("Sorry, try again! You still have",
                      no_of_tries, "tries left.")
            else:
                print("Sorry, you have no tries left. The correct number was", secret)

    print("Your balance is:", balance)

    if balance <= 0:
        print("You have no balance left! Game over.")
        break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing! Your final balance is:", balance)
        break
