# pylint: skip-file

# Membership operators - if, if not.
# Identity operators compare the memory locations of two objects.

intA = 10
intB = 20

arrintValues = [ 1, 2, 3, 4, 5 ]

if( intA in arrintValues ) :
	print 'A is in list.'
else :
	print 'A is not in list.'

if( intB not in arrintValues ) :
	print 'B is not in list.'
else :
	print 'B is in list.'

intB = 4
if( intB in arrintValues ) :
	print 'B is in list.'
else :
	print 'B is not in list.'
