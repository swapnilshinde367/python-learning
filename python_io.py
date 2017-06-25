# pylint: skip-file
# I/O functions
import os

# take input from keyboard
# strInput = raw_input( 'Enter somthing here....\n' )
# print strInput

# # take input from keyboard as python expression, e.g you can enter 10+20 it will print 30
# strInput = input( 'Enter what do you want to execute here....\n' )
# print strInput

# Open File for reading
objFile = file( 'secret_messages/a.txt', 'r' )
# Prints name
print objFile.name
# Prints file pointer location
print objFile.tell()

# Read function can take arguments, which is number, which tells how many characters to read and reads form first character.
# If left blank it tries to read whole file
strFileContent = objFile.read()
print strFileContent

# Close file
objFile.close()

# Open File for reading and writing
objFile = file( 'secret_messages/a.txt', 'w+' )
objFile.write( 'I came from python program' )
print objFile.read()
objFile.close()

# Open File for reading and appending
objFile = file( 'secret_messages/a.txt', 'a+' )
objFile.write( 'I came from python program' )
print objFile.read()
objFile.close()

# Create file and rename it
objFile = file( '123.txt', 'w+' )
objFile.write( 'what?' )
os.rename( '123.txt', '321.txt' )

# Delete the file
os.remove( '321.txt' )

# Create directory
os.mkdir( 'TestDir' )
# Change directory
os.chdir( 'TestDir' )
# Get present working  directory
print os.getcwd()

# Go back to parent directory, so you can delete TestDir
os.chdir( '../' )

# Delete directory
os.rmdir( 'TestDir' )