# pylint: skip-file
# Import parent class
# Create sub class, inherit parent class' variables, inherit parent's instance methods.

from CEmployee import CEmployee

class CDeveloper(CEmployee):

    strExpertise = ''

objDeveloper = CDeveloper()

objDeveloper.strFirstName   = 'Rey'
objDeveloper.strLastName    = 'Mysterio'
objDeveloper.strExpertise   = 'Python'

objDeveloper.handleCreateEmailAddress()

print(objDeveloper.strEmailAddress)
print(objDeveloper.strExpertise)