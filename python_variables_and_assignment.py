# pylint: skip-file

# variables, their assignment and deleting them

intA = 10
print intA

fltMiles = 10.28
print fltMiles

strName = 'Swapnil Shinde'
print strName

intA, fltMiles, strName = 10, 10.28, 'Swapnil Shinde'
print intA
print fltMiles
print strName
# OR
print intA, fltMiles, strName

# Deleting variable from memory
del intA
del fltMiles
del strName

# possible with multiple variables on one line as follows
# del intA, fltMiles, strName

# this will show error NameError: name 'intA' is not defined
print intA
print fltMiles
print strName