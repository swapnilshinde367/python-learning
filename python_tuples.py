# pylint: skip-file

# tuples, their operations, concat, repeat, string selctive elements

# tuples are nothing but lists but read only which cannot be updated

tuple = ('abcd', 345 , 2.23, 'randy', 70.2 )
tinytuple = ( 123, 'orton' )

# Print whole tuple
print tuple

# Print first element
print tuple[1]

# Print first to fourth element
print tuple[1 : 4]

# Print second to last element
print tuple[2 :]

# Concat the 2 tuples
print tuple + tinytuple

# Print the tuple 2 times
print tinytuple * 2

# Following throws an error
tinytuple[2] = 678