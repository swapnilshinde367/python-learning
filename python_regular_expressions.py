# pylint: skip-file
# Regular Expressions.

import re

strDescription = 'A is always smarter than B'

# re.match: matches RE pattern and returns matching object on success "none" on failure.
# re.M is match multiline
# re.Iis match case insensitive
objMatches = re.match( r'(.*) is (.*?) .*', strDescription, re.M | re.I )

# Print all matching groups using groups()
print objMatches.groups()

# Print given string or matching groups using group(integer)
# Print the string given to match
print objMatches.group()
# Print the first match
print objMatches.group(1)
# Print the second match
print objMatches.group(2)

# re.search: searches string for first RE pattern and returns matching object on success "none" on failure.
objMatches = re.search( r'(.*) is (.*?) .*', strDescription, re.M | re.I )

print objMatches.groups()

print objMatches.group()
print objMatches.group(1)
print objMatches.group(2)

# match searches for pattern only in beginning of string and search checks for match anywhere in string.

# Following will print result only from search.
objMatches = re.match( r'B', strDescription, re.M | re.I )
if objMatches :
	print objMatches.group()
else:
	print 'Nothing from match'

objMatches = re.search( r'B', strDescription, re.M | re.I )
if objMatches :
	print objMatches.group()
else:
	print 'Nothin from search'

# sub: find and replace pattern
strPhoneNumber = '123-1234-2345'
# remove all non digits
strResult = re.sub( r'\D', '', strPhoneNumber )
print strResult

# remove everything after #
strResult = re.sub( r'#.*$', '', strPhoneNumber )
print strResult