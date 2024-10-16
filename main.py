# Programmers: Ethan D'Souza & Andrew Leimbach
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/16/2024
# Lab Assignment: 05
# Problem: Build a simulation of an ATM (Automatic Teller Machine), where users can View their balance, Deposit (e.g. add money to the account), or Withdraw (e.g. take money from the account).
# Purpose: Designing and programming loops, Re-using many of the other aspects of Python we've learned so far, Testing code, Error checking

# ATM Simulation Program


# Welcome message explaining the program
print("Welcome to the ATM Simulator!")
print("Your initial balance is $1000.")

# Initial balance is set to $1000
balance = 1000

# Start a loop that will keep going until the user decides to exit
while True:
    # Show the options for the user
    print("What would you like to do?")
    print("D - Deposit money")
    print("W - Withdraw money")
    print("V - View your balance")
    print("E - Exit the program")

    # Get the user's choice (upper case so it works for both lower and upper case)
    choice = input("Enter your choice (D/W/V/E): ").upper()

    # If user chooses to deposit money
    if choice == 'D':
        deposit_amount = float(input("Enter the amount to deposit: "))

        # Check if the deposit amount is valid (not negative)
        if deposit_amount < 0:
            print("Error: You can't deposit a negative amount. Try again.")
        else:
            balance += deposit_amount  # Add the deposit to the balance
            print("{deposit_amount:.2f} deposited successfully.")
            print(f"Your new balance is: {balance:.2f}")

    # If user chooses to withdraw money
    elif choice == 'W':
        withdraw_amount = float(input("Enter the amount to withdraw: "))

        # Check if the withdrawal amount is valid (not negative)
        if withdraw_amount < 0:
            print("Error: You can't withdraw a negative amount. Try again.")
        else:
            # Check if the withdrawal would result in an overdraft
            if withdraw_amount > balance:
                print("Error: Insufficient funds. You can't withdraw more than your balance.")
            else:
                balance = balance - withdraw_amount  # Subtract the withdrawal from the balance
                print(f"{withdraw_amount:.2f} withdrawn successfully.")
                print(f"Your new balance is: {balance:.2f}")

    # If user chooses to view the balance
    elif choice == 'V':
        print(f"Your current balance is: ${balance:.2f}")

    # If user chooses to exit the program
    elif choice == 'E':
        print("Thank you for using the ATM. Goodbye!")
        break  # End the loop and exit the program

    # If user enters an invalid choice
    else:
        print("Error: Invalid choice. Please enter D, W, V, or E.")
