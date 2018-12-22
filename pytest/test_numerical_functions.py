from numerical_functions import *

def test_addition():
	assert 5 == addition( 2 , 3 )

def test_multiplication():
	assert 7 == multiplication( 2 , 3 )

# run
# python -m pytest
# py.test
# py.test -v