"""
Example runs:

Enter a number: {10}
Enter a math operator: {+}
Enter another number: {5}
10.0 + 5.0 = 15.0

Enter a number: {7.5}
Enter a math operator: {-}
Enter another number: {2.5}
7.5 - 2.5 = 5.0

Enter a number: {2}
Enter a math operator: {*}
Enter another number: {4}
2.0 * 4.0 = 8.0

Enter a number: {10}
Enter a math operator: {/}
Enter another number: {2}
10.0 / 2.0 = 5.0
"""

# Ask the user for the first number, and convert it to a float
first_number = float(input("Enter a number: "))

# Ask the user for the operator
operator = input("Enter a math operator: ")

# Ask the user for the second number, and convert it to a float
second_number = float(input("Enter another number: "))

# Perform the calculation depending on what operator the user chose
if operator == "+":
    result = first_number + second_number

elif operator == "-":
    result = first_number - second_number

elif operator == "*":
    result = first_number * second_number

elif operator == "/":
    result = first_number / second_number

# Print out the resulting equation
print(first_number, operator, second_number, "=", result)