"""
Remember this is a comment and is not part of the code!

Example runs:

Run 1:

Hello! Please enter your name: {Jake}

Hello, Jake ! What would you like to do?
1. View my balance
2. Withdraw money
3. Deposit money

Enter the number for your choice: {1}

Your balance is $100 .00.


Run 2:

Hello! Please enter your name: {Alice}

Hello, Alice ! What would you like to do?
1. View my balance
2. Withdraw money
3. Deposit money

Enter the number for your choice: {2}

Enter the amount you would like to withdraw: {50}

Your balance is now $50 .00.


Run 3:

Hello! Please enter your name: {Bob}

Hello, Bob ! What would you like to do?
1. View my balance
2. Withdraw money
3. Deposit money

Enter the number for your choice: {3}

Enter the amount you would like to deposit: {100}

Your balance is now $200 .00.
"""

# Set the initial balance
balance = 100

# Get the name of the user
name = input("Hello! Please enter your name: ")
print()

# Print out the options for the user
print("Hello,", name, "! What would you like to do?")
print("1. View my balance")
print("2. Withdraw money")
print("3. Deposit money")
print()

# Get the user's choice
choice = int(input("Enter the number for your choice: "))
print()

# Check what the user wants to do
# If they want to view their balance
if choice == 1:
    print("Your balance is $", balance, ".00")


# If they want to withdraw money
if choice == 2:
    # Get the amount they want to withdraw
    withdraw = int(input("Enter the amount you would like to withdraw: "))

    # Subtract the amount from the balance (You can also do `balance -= withdraw`)
    balance = balance - withdraw

    # Print out the new balance
    print("Your balance is now $", balance, ".00")


# If they want to deposit money
if choice == 3:
    # Get the amount they want to deposit
    deposit = int(input("Enter the amount you would like to deposit: "))

    # Add the amount to the balance (You can also do `balance += deposit`)
    balance = balance + deposit

    # Print out the new balance
    print("Your balance is now $", balance, ".00")