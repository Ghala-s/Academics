"""
CS1026a 2023
Assignment 01 Project 01 - Part A
Ghala Basaad
251384549
gbasaad
Oct 02, 2023
"""

# Printing App Header
print("Project One (01) - Part A : Fibonacci Sequence")

a = 0  # This Var will hold first value
b = 1  # This Var will hold second value
counter = 0  # This Var is our loop counter

# getting input from the user, and assign it to a variable
num = int(input("Sequence ends at: "))

# Loop from 0 until counter reaches to user input number (inclusive)
while counter <= num:

    # Printing the current number to user
    print(str(counter) + ":", str(a), f"{a:,}")
    c = a + b  # Calculating the next number
    a = b  # Adjusting the first number
    b = c  # Save the next number
    counter += 1  # Increment counter
print()

# Printing App Footer
print("END: Project One (01) - Part A")
print("Ghala Basaad gbasaad 251384549")


