my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
leng=len(my_list)-1
for i in range(leng):
    if my_list[i] == my_list[i+1]:
        del my_list[i+1]
        leng=len(my_list)-1

#
print("The list with unique elements only:")
print(my_list)
