#######             LOOPS             ######

#   Loop: Performing a certain part of the code more than once is called a loop.

####      WHILE LOOP         ###
'''
    while conditional_expression:
        instruction_1
        instruction_2
        instruction_3
        instruction_4

        .
        .
        .
        instruction_n

If there is no instruction, nothing will happen.

While loop repeats the execution as long as the condition evaluates to TRUE.

If the condition = FALSE the body of the loop will not be executed.

######    SIMPLIFICATIONS    ######

while number != 0:
and
while number:

if number % 2 == 1:
and
if number % 2:


#### COUNTER ####

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

'''


####      FOR LOOP         ###

'''
In the for loop there is no condition like in the while loop:

These are checked internally, the variable after the 'for' keyword is a CONTROL VARIABLE of the loop
It counts the loops turns automatically.

'in' keyword describes the possible values being assigned to the control variable

'range()' it generates and feeds the values to the control variable

for i in range(100):
    # do_something()
    pass
    
for i in range(10):
    print("The value of i is currently", i)


The 'i' will be fed the values from 0,1,2,3,4...98,99 (not 100)

'pass' it is an empty instruction, for loop requires ATLEAST 1 INSTRUCTION INSIDE THE BODY

#####    range()    #####

1st argument = Tells the starting number
2nd argument = Tells the stopping number (it doesnt include this number)
3rd argument = Tells the step between the 2 numbers

range(2,8) can be given 2 arguments as well (ONLY INTEGERS accepted)

range() will always sort it out in ascending order (cant be forced otherwise)

2nd argument > 1st argument (Always) (If this is done there will be NO ERROR AND NO OUTPUT)


i = 2,3,4,5,6,7 (not 8)

for i in range(2, 8, 3):
    print("The value of i is currently", i)

i = 2, 5 (difference between them is 3)


# Here the expo variable is acting as a counter 

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

import time
for a in range(5):
    time.sleep(1)
    print('Mississippi')

'''

####     BREAK AND CONTINUE        ###


'''
BREAK

1. if it appears uneccessary to conttinue the loop, stop execution

2. Exits immediately, and unconditionally ends the loop, executes nearest inst after it 

CONTINUE

1. start the next turn without completing the execution of current turn

2. Behaves as if the program has suddenly reached the end of the body, next turn
    is started and condition is tested immediately.

'''

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word=input('Enter a word: ')
user_word=user_word.upper()


for letter in user_word:
    # Complete the body of the for loop.
    if (letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U'):
        continue
    print(letter)



word_without_vowels = ""

user_word=input('Enter a word: ')
# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word=user_word.upper()


for letter in user_word:
    # Complete the body of the loop.
    if (letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
        continue
    word_without_vowels += letter

print(word_without_vowels)
# Print the word assigned to word_without_vowels.



################################ WHILE and ELSE ################

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


#When the condition for the while does not match then the 'else' is executed

################################ FOR and ELSE ################
for i in range(5):
    print(i)
else:
    print("else:", i)


    # For some reason this prints out 1,2,3,4 else:4
    # Why ?

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

    # This makes sense as range(2,1) will fail.



blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0
new_blk = 1
blk_in_stk = 0
flag = 0

while blocks:
    blk_in_stk +=  new_blk
    new_blk +=  1
    height +=  1
    if blk_in_stk > blocks:
        flag += 1
        height = 0
        new_blk = 1 + flag
        blk_in_stk = 0
    if blk_in_stk == blocks:
        break


print("The height of the pyramid:", height)






c0=int(input("Enter a Number: "))
step=1

while c0 != 1:
    if(c0%2)==0: # If c0 is EVEN
        c0 = c0 /2
        step += 1
        print(int(c0))
    
    else:           # If c0 is ODD
        c0 = 3*c0 + 1
        step += 1
        print(int(c0))

print('Setps: ', step)




for i in range(1,11):
    if (i%2)!=0:
        print(i)

x=1
while x < 11:
    if (x%2)!=0:
        print(x)
    x+=1

for ch in "akshay.dandgaval@gmail.com":
    if ch == "@":
        break

    print(ch,end="")


print('\n')
for digit in "04564056465404654045646404532":
    if digit == "0":
        print('x',end='')
        continue
        
    print(digit,end='')



