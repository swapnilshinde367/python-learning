# pylint: skip-file
# Create class.
# Create class variables,instance methods.
# Magic methods for class.

class CEmployee:

	intSalary		= 0
	strFirstName	= ''
	strEmailAddress	= ''
	strLastName		= ''

	def __init__(self):
		pass

	def handleCreateEmailAddress( self ):
		self.strEmailAddress = self.strFirstName + '.' + self.strLastName + '@' + 'company.com'

	def __repr__( self ):
		return '{} - {}'.format( self.strFirstName, self.strLastName)

	def __str__( self ):
		return '{} - {}'.format( self.strFirstName, self.strLastName)

objEmployee1 = CEmployee()
objEmployee1.strFirstName	= 'John'
objEmployee1.strLastName	= 'Cena'
objEmployee1.intSalary		= 1500

objEmployee2 = CEmployee()
objEmployee2.strFirstName	= 'Randy'
objEmployee2.strLastName	= 'Orton'
objEmployee2.intSalary		= 2000

# objEmployee1.handleCreateEmailAddress()

# objEmployee2.handleCreateEmailAddress()

# print( objEmployee1.strEmailAddress )

# print( objEmployee2.strEmailAddress )

# class magic methods
print( objEmployee1.__repr__() )
print( objEmployee1.__str__() )