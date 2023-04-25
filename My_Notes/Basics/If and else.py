#######             DECISION             ######


# Equality Operator (==)

# Its a BINARY operator and needs 2 arguments and checks if they are equal

print(2 == 2)   # True
print(2 == 2.)   # True

# Inequality Operator (!=)

# It compares the values of 2 operands and result of the comparison is either True or False


## Comparison Operator

# Greater than or Equal to (>=)
# Less than or Equal to (<=)

'''
1 (Unary): + -
2          **
3          * / // %
4 (Binary): + -
5           < <= > >=
6           == !=
'''


###         CONDITIONAL STATMENTS           ###


#Rules:

#   'if'
#   One or more white space
#   Expression (can either be True or False)
#   ':' followed by new line
#   An Indented set of instructions if the expression is true (use 4 spaces or Tab)
#   Indentation should be same on all the lines
#   'else' also has a ':' after it no space

'''

  if the_weather_is_good:
     go_for_a_walk()
  have_lunch()

--------------ELSE----------------------

  if true_or_false_condition:
    perform_if_condition_true
  else:
    perform_if_condition_false

-------------NESTED IF-----------------------

   if the_weather_is_good:
        if nice_restaurant_is_found:
            have_lunch()
        else:
            eat_a_sandwich()
   else:
        if tickets_are_available:
            go_to_the_theater()
        else:
            go_shopping()

--------------ELIF----------------------

   if the_weather_is_good:
        go_for_a_walk()
   elif tickets_are_available:
        go_to_the_theater()
   elif table_is_available:
        go_for_lunch()
   else:
        play_chess_at_home()

Only when the the if statement is FALSE it will check the elif statements

--------------ONLY IF----------------------

    x = 10

    if x > 5:  # True
        print("x > 5")

    if x > 8:  # True
        print("x > 8")

    if x > 10:  # False
        print("x > 10")

    else:
        print("else will be executed")


Here all the if statements will be checked, unlike the above
            
'''

# 'else' is always the last branch of the cascade regardless of using 'elif'
# 'else' is OPTIONAL
# If there is an 'else' branch in the cascade, only 1 of all the branches will be executed
# 

'''

if number1 > number2: larger_number = number1
else: larger_number = number2

The above is allowed in python
'''






