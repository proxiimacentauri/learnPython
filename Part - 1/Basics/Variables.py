#######             VARIABLES             ######


# Variable: Its a named location reserved to store values in the memory. A variable is created or initialized
#           automatically when you assign a value to it for the first time

# Python is a dynamically-typed language where the variables dont need to be declared.

# RULES

#1: Name should be: upper/lowercase letters, digits, '_'
#2: Must begin with a letter
#3: The Underscore Char is a letter '_' = LETTER
#4: Upper and lower case are different akshay and AKSHAY will be 2 diff var. names
#5: Dont use reserved words for var names like 'print' cant be a var name

# Example

## CORRECT

# MyVariable, i, t34, Exchange_Rate, counter,
# days_to_christmas, TheNameIsSoLongThatYouWillMakeMistakesWithIt, _

# Adiós_Señora, sûr_la_mer, Einbahnstraße, переменная


## INCORRECT

# 10t, Exchange Rate

### RESERVED KEYWORD   ###

#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def',
# 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
# 'while', 'with', 'yield']

var=1
print(var)

account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)

# You can use the '+' sign to combine the text and variables

var = "3.6.0"
print("Python version: " + var) # This is only valid because var is a string

var = 3.6             # Use this for a FLOAT or INT
print("Python version: ", var)

a = '1'
b = "1"
print(a + b)

print(123+0.0)

## Python treats the sign (=) not as equal to, but as assign a value.


## SHORTCUT OPERATORS

# If op is a two-argument operator (this is a very important condition) and the operator is used in the following context:

# variable = variable op expression
# variable op= expression

# i = i + 2 * j ⇒ i += 2 * j
# var = var / 2 ⇒ var /= 2
# rem = rem % 10 ⇒ rem %= 10
# j = j - (i + var + rem) ⇒ j -= (i + var + rem)
# x = x ** 2 ⇒ x **= 2
