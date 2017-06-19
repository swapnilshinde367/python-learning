# pylint: skip-file

# while loop, while..else.

intCount = 0

while( intCount < 10 ) :
	print intCount
	intCount = intCount + 1


intCount = 10

while( intCount > 0 ) :
	print intCount
	intCount = intCount - 1
else:
	print 'Now reached to 0'