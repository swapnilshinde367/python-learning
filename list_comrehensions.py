listNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Getting 'n' for each 'n' in listNumebers
# usual way
# new_list = []
# for n in listNumbers :
# 	new_list.append( n )
# print( new_list )

# list comprehensions
new_list = [ n for n in listNumbers ]
print( new_list )

# squaring numbers
new_list = [ n * n for n in listNumbers ]
print( new_list )

# using map + lambda
# new_list = map( lambda n: n*n, listNumbers )
# for n in new_list :
# 	print( n, end=' ' )

# Get 'n' for each 'n'  if its even
new_list = [n for n in listNumbers if n%2 == 0]
print( new_list )
# new_list = filter( lambda n: n%2 == 0, listNumbers )
# for n in new_list :
# 	print( n, end=' ' )

# nested for loops
# I want pair of (letter, number) of for each letter in 'abcd' and for each number in 0123
new_list = []
# for letter in 'abcd' :
# 	for number in range( 4 ) :
# 		new_list.append( (letter, number) )
# print( new_list )
new_list = [ (letter, number) for letter in 'abcd' for number in range( 4 ) ]
print( new_list )