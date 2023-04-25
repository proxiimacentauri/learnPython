make_asc=[65,8,5,6,1,86,21,786,123,4,2,53,53,42,12,78679,45]
print('Unsorted List:', make_asc)
swap=True
while swap:
    swap=False
    for i in range(len(make_asc)-1):   # here i = 0,1,2,3...(17-1)
        if make_asc[i] > make_asc[i+1]:
            make_asc[i], make_asc[i+1] = make_asc[i+1], make_asc[i]
            swap = True
            
print('Sorted List:', make_asc)
