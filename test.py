# pylint: skip-file
# draw different shapes using turtle
#TODO: Implement the nearest_square function

def nearest_square( intNum ) :

	intCount = 1

	while( intCount**2 <= intNum ) :
		intCount = intCount + 1

	intCount = intCount -1

	return intCount**2

print ( nearest_square(40) )