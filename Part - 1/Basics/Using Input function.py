#######             input()             ######



# It is a function is able to read data entered by the
# user and to return the same data to the running program.

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# It is also possible to input data using a voice or an image
# Simplest way to invoke input() is without any arguments, where it will switch to console input mode
# it will be a BLINKING CURSOR on the console. Press ENTER when done typing.
# Assignment to a variable is important


anything = input("Please Input Something: ")
print("Hmm...", anything, "...Really?")

# Result of an input() is a STRING ---- IMP
# Therefore you cant use it as a INT or a FLOAT operator.


anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)


# Use int() and float() and str()

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

anything = float(input("Enter a number: "))
something = str(anything ** 2.0)
print(anything, "to the power of 2 is" + something)



# Concatination Operator (+) when both its arguments are strings


fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# Replicaiton (*) : When applied to a string and a number becomes a replication operator


# "James" * 3 gives "JamesJamesJames"
# 3 * "an" gives "ananan"
# 5 * "2" (or "2" * 5) gives "22222" (not 10!)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
