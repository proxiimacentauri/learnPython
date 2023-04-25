
#Python does not like to place 2 or more lines of code in 1 line 

##print('A') print('Ak')

# Way to create a newline
print()
print('Akshay\nAishwarya')

# Print function accepting  2 arguments, print automatically puts in space
# between AkshayspaceAishwarya and outputs them all one 1 line

print('Akshay','Aishwarya')
print('Akshay',' Aishwarya')

# Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted
# after the first, the third is outputted after the second, etc.

# Keyword arguments =  ones whose meaning is not dictated by their location,
#but by a special word (keyword) used to identify them


print('Name is','Akshay.',end='End')
print('Akshay Dandgaval')

# Also there is NO SPACING between 'Akshay.End' cause of the end keyword argument
# By default when end= Not specified it is end='\n'


#The arguments of the the print() can be seperated by any aything

print('My','name','is','Akshay.',sep='+')
print('My','name','is','Akshay.',sep=' ')

# Example of Keyword arguments:

print('Programming','Essentials','in',sep='***',end='...')
print('Python')
