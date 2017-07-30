# pylint: skip-file
# Create child class

from python_parent_class_example import Employee

class SubEmployee( Employee ) :
	'Common class for sub-employee'

	strDepartment = ''

	def __init__( self, strName, intSalary, strDepartment ) :
		Employee.__init__( self, strName, intSalary )
		self.strDepartment = strDepartment

# Overriding parent method
	def handleEmployeeDetails( self ) :
		print self.strName + ' is from department ' + self.strDepartment + ' has salary: ' + str( self.intSalary )

objSubEmployee = SubEmployee( 'Swapnil', 1000, 'Development' )
objSubEmployee.handleEmployeeDetails()

# # Changing salary
# objEmployee.intSalary = 2000

# objEmployee.handleEmployeeDetails()