def add( a, b ) :
	return a + b

def multiplication( a, b ) :
	return a * b

def divide( a, b ) :
	if 0 == b :
		raise ValueError( 'Can not divide by 0' )
	return a / b