# pylint: skip-file
# Create parent class

class Employee :
	'Common class for employee'

	strName = ''
	intSalary = 0

	def __init__( self, strName, intSalary ) :
		self.strName = strName
		self.intSalary = intSalary

	def handleEmployeeDetails( self ) :
		print self.strName + ' has salary = ' + str( self.intSalary )