# pylint: skip-file
# Getter, Setter.

class CEmployee:

	intSalary		= 0
	# strFullName		= ''
	strLastName		= ''
	strFirstName	= ''
	# strEmailAddress	= ''

	@property
	def strFullName( self ):
		return '{} {}' . format( self.strFirstName, self.strLastName )

	@property
	def strEmailAddress( self ):
		return '{}.{}@company.com' . format( self.strFirstName, self.strLastName )

	@strFullName.setter
	def strFullName( self, strFullName ):
		strFirstName, strLastName = strFullName.split( ' ' )
		self.strFirstName = strFirstName
		self.strLastName = strLastName

objEmployee1 = CEmployee()
objEmployee1.strFirstName	= 'John'
objEmployee1.strLastName	= 'Cena'
objEmployee1.intSalary		= 1500

print( objEmployee1.strFullName )
print( objEmployee1.strEmailAddress )

objEmployee1.strFullName = 'Randy Orton'

print( objEmployee1.strFullName )
print( objEmployee1.strFirstName )
print( objEmployee1.strEmailAddress )