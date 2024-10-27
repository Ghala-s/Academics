"""
CS1026a 2023
Assignment 01 Project 01 - Part B
Ghala Basaad
251384549
gbasaad
Oct 02, 2023
"""

# Printing App Header
print("Part One - Project B: Prime Choice")
print()

start_num = int(input("Prime Numbers starting with: "))  # This Var holds our starting value
end_num = int(input("and ending with: "))  # This Var holds our ending value
temp = 0  # This Var is our temporarily holder
print()

if start_num > end_num:  # Checking if the user enters values incorrectly
    print("Incorrect Input: {} is greater than {}".format(start_num, end_num))
    print("The numbers have been automatically switched.")
    counter = start_num
    start_num = end_num
    end_num = counter
    print()

print("Prime numbers in the range from: {} and {} are:".format(start_num, end_num))

# Looping from the start num to the end number inclusively
for i in range(start_num, end_num + 1):
    for j in range(2, i):
        if i % j == 0:
            break  # This is not a prime number, move on to next number
    else:  # It could be a prime Number
        if i > 1:  # Checking if the value is greater than one
            print(i, "is prime")  # Print to screen as this is a prime number

# App Footer
print()
print("End: Project One (01) - Part B")
print("Ghala Basaad gbasaad 251384549")
