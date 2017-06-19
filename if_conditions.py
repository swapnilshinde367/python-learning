# pylint: skip-file

# if, if..else, if..elif..else, if...if..else...else(nested if else)


intA = 100

if( intA > 100 ) :
	print 'Greater than 100'
	if( 0 == intA%2 ) :
		print 'Greater than 100 and even'
	else:
		print 'Greater than 100 and odd'
elif( intA < 100 ):
	print 'Lesser than 100'
	if( 0 == intA%2 ) :
		# The pass statement in Python is used when a statement is required syntactically,
		# but you do not want any command or code to execute.
		pass
	else:
		print 'Lesser than 100 and odd'
else:
	print 'Definitely 100'