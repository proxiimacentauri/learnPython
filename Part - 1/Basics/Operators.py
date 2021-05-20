#######             OPERATORS             ######

# Operator = Its a symbol of the programming language, which is able to operate on the values.

# Example:  + - * / // % **

# Expression = When data and operators are connected together they form expressions.
#               Simplest expression is a litral


# Exponent (**): To represent 8^5 we do that by 8**5

print(8**5)
print(8**5.2)


# The result produced by a division operator is always a FLOAT

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)


# Integer Division (//): its result lacks the fractional part - it's absent (for integers), or is always equal to zero (for floats);
#                           this means that the results are always rounded


print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

# The answer should be 1.5 but it is rounded to 1
# even if the ans is 1.9 it will be rounded to 1

print(6 // 4) 
print(6. // 4)


#The result of integer division is always rounded to the nearest integer value that is less
# than the real (not rounded) result.


# Remainder (Modulo) (%): Remainder left after integer division

print (14 % 4)


# Unary and Binary operator

print(-4 - 4)
print(+3)

# Here the (-4) the '-' sign is a unary operator and in the expression '-4 - 4' its binary
# (+3) the '+' is also a unary operator




#### Binding of Operators:  left-sided binding, which means that the calculation of the
#                          expression is conducted from left to right.

print(9 % 6 % 2)    # LEFT SIDE BINDING
print(2 ** 2 ** 3)   # RIGHT SIDE BINDING




#### PRIORITY   ####
# Subexpressions in parentheses are always calculated first.

# (* and %) have the same priority, left binding takes place

print(2 * 3 % 5)

#1 (Unary): + -
#2          **
#3          * / // %
#4 (Binary): + -

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

### IMP: the last one ^^^


print((2 % -4), (2 % 4), (2 ** 3 ** 2))


# Here 2*b is taking priority

a = 6
b = 3
a /= 2 * b
print(a)
