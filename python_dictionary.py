# pylint: skip-file

# Dictionary, its operations, add value, delete value, print whole dictionary, print only values, print only keys

# Dictionary is like an associative array, a key value pair array

arrmixDictionary = { 'one' : 1, 'two' : 2, 'three' : 3, 4 : 'four', 5 : 'five' }

print arrmixDictionary

# Adding element to dictionary
arrmixDictionary[6] = 'This is six'
print arrmixDictionary

# Print value at key "three"
print arrmixDictionary['three']

# Print value at key "4"
print arrmixDictionary[4]

# Delete value at key "6"
del arrmixDictionary[6]

# Print all keys
print arrmixDictionary.keys()

# Print all values
print arrmixDictionary.values()