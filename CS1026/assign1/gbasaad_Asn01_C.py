"""
CS1026a 2023
Assignment 01 Project 01 - Part C
Ghala Basaad
251384549
gbasaad
Oct 05, 2023
"""

# Printing App Header
print("Project One (01) - Part C: The Moore the Merrier")

# Prompting the user for input values, and assigning it to a variable
trans_num = int(input("Starting Number of transistors: "))  # This Var will hold the starting numbers of transistors
start_year = int(input("Starting Year: "))  # This Var will hold the starting year
years_num = int(input("Total Number of Years: "))  # This Var will hold the total numbers of years
end_year = start_year + years_num     # This Var will hold the terminating year
print()
print("YEAR : TRANSISTORS : FLOPS:")

# The 'while' loop will print out a table of values
while start_year <= end_year:
    flops = trans_num* 50

    # 'if-elif' statments will helps us determine the appropriate unit for 'flops' and store the result in 'flop_unit'
    # The result of the calculation is limited to two decimal places
    if flops<10**3:
        flop_unit = str(f"{flops:.2f}") + " FLOPS"
    elif flops<10**6:
        flop_unit = str(f"{flops/10**3:.2f}") + " kiloFLOPS"   # kiloFLOPS = 10^3 Flops
    elif flops<10**9:
        flop_unit = str(f"{flops/10**6:.2f}") + " megaFLOPS"   # megaFLOPS = 10^6 FLOPS
    elif flops<10**12:
        flop_unit = str(f"{flops/10**9:.2f}") + " gigaFLOPS"   # gigaFLOPS = 10^9 FLOPS
    elif flops<10**15:
        flop_unit = str(f"{flops/10**12:.2f}") + " teraFLOPS"   # teraFLOPS = 10^12 FLOPS
    elif flops<10**18:
        flop_unit = str(f"{flops/10**15:.2f}") + " petaFLOPS"   # petaFLOPS = 10^15 FLOPS
    elif flops<10**21:
        flop_unit = str(f"{flops/10**18:.2f}") + " exaFLOPS"   # exaFLOPS = 10^18 FLOPS
    elif flops<10**24:
        flop_unit = str(f"{flops/10**21:.2f}") + " zettaFLOPS"   # zettaFLOPS = 10^21 FLOPS
    elif flops<10**27:
        flop_unit = str(f"{flops/10**24:.2f}") + " yottaFLOPS"   # yottaFLOPS = 10^24 FLOPS

    print(f"{start_year} {trans_num:,} {flop_unit} {flops:,}")

    # Adding '2' for an increment each two years
    start_year += 2
    trans_num *= 2


# Printing App Footer
print()
print("END: Project One (01) - Part C")
print("Ghala Basaad gbasaad 251384549")

