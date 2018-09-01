# pylint: skip-file

def handleOuterFunction( function_name ) :

	def handleInnerFunction() :
		return function_name()

	return handleInnerFunction

def display() :
	print 'Yo'

my_func = handleOuterFunction( display )

my_func()