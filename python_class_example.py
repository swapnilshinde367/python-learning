# pylint: skip-file
# Create class.
# Create class variables, instance methods.

class Employee :
	'Common class for employee'

	strName = ''
	intSalary = 0

	def __init__( self, strName, intSalary ) :
		self.strName = strName
		self.intSalary = intSalary

	def handleEmployeeDetails( self ) :
		print self.strName + ' has salary = ' + str( self.intSalary )

objEmployee = Employee( 'Swapnil', 1000 )
objEmployee.handleEmployeeDetails()

# Changing salary
objEmployee.intSalary = 2000

objEmployee.handleEmployeeDetails()