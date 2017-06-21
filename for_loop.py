# pylint: skip-file

# for loop, use of else in for loop

arrstrName = 'Swapnil'
for strLetter in arrstrName :
	print strLetter


arrstrFruitNames = [ 'Mango', 'Apple', 'Guava', 'Jackfruit' ]
for strFruitName in arrstrFruitNames :
	print strFruitName

# For index
arrstrFruitNames = [ 'Mango', 'Apple', 'Guava', 'Jackfruit' ]
for intIndex in range( len( arrstrFruitNames ) ) :
	print arrstrFruitNames[intIndex]

# Use of else: Else in for loop will be called when the all the iterations are completed it cannot enter the if condition

for intI in range( 10, 20 ) :
	for intJ in range( 2, intI ) :
		if( 0 == intI % intJ ) :
			print  '%d = %d * %d' % ( intI, intJ, intI/intJ )
			break
	else :
		print str( intI ) + ' is prime'