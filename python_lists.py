# pylint: skip-file

# lists, their operations, concat, repeat, string selctive elements

list = [ 'abcd', 345 , 2.23, 'randy', 70.2 ]
tinylist = [ 123, 'orton' ]

# Print whole list
print list

# Print first element
print list[1]

# Print first to fourth element
print list[1 : 4]

# Print second to last element
print list[2 :]

# Concat the 2 lists
print list + tinylist

# Print the list 2 times
print tinylist * 2

# Use negative index

print list[-3]

# Skip the value using "step"
# This prints as it is by default
print list[0:4:1]

# Skip every second value
print list[0:4:2]

# Use negative step
print list[-1:0:-1]