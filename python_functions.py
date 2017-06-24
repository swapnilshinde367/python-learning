# pylint: skip-file
# defining a function and calling it with various methods

def handlePrintInfo( strName = 'Swapnil', intAge = 100 ) :
	print 'Name is ' + strName + ' and age is ' + str( intAge )

# Default arguments
handlePrintInfo()

# Normal call
strStudentName = 'John'
intStudentAge = 20
handlePrintInfo( strStudentName, intStudentAge )

# Keyword arguments, it allows to send parameters in out of order fashion, it identifes the variables by names
handlePrintInfo( intAge=25, strName='Randy' )

# Keyword arguments with default parameters
handlePrintInfo( intAge=25 )

# Variable length functions
# if number of arguments are not fixed, then we can use tuple to define such functions

# With one fixed argument
def handlePrintMultipleNumbers( intA, *arrintNumbers ) :
	print intA
	for intNumber in arrintNumbers :
		print intNumber

handlePrintMultipleNumbers( 10 )
handlePrintMultipleNumbers( 10, 20, 30, 40, 50 )

# With no fixed argument
def handlePrintMultipleNumbers( *arrintNumbers ) :
	for intNumber in arrintNumbers :
		print intNumber

handlePrintMultipleNumbers( 10 )
handlePrintMultipleNumbers( 10, 20, 30, 40, 50 )