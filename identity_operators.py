# pylint: skip-file

# Identity operators - is, is not.
# Identity operators compare the memory locations of two objects.

intA = 10
intB = 10
if( intA is intB ) :
	print 'A and B have same identity.'
else :
	print 'A and B does not have same identity.'

# id() gives memory location
if( id( intA ) == id( intB ) ) :
	print 'A and B have same identity.'
else :
	print 'A and B does not have same identity.'

intB = 20
if( intA is intB ) :
	print 'A and B have same identity.'
else :
	print 'A and B does not have same identity.'

if( intA is not intB ) :
	print 'A and B does not have same identity.'
else :
	print 'A and B have same identity.'