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
