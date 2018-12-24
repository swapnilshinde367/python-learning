import pytest
import sys
import numerical_functions

# skip if function to skip test based on if condition
# @pytest.mark.skipif( sys.version_info < ( 3, 5 ), reason = 'Testing Python version' )
def test_addition() :
	assert 5 == numerical_functions.addition( 2 , 3 )

# skip test function
# @pytest.mark.skip( reason = 'Skipping Test' )
def test_multiplication() :
	assert 6 == numerical_functions.multiplication( 2 , 3 )


# Creating a custom tag so we can run specific tests using that marker
@pytest.mark.two
def test_dividebytwo() :
	assert 2 == numerical_functions.dividebytwo( 4 )

@pytest.mark.five
def test_dividebyfive() :
	assert 2 == numerical_functions.dividebyfive( 4 )

# to run use following commands
# python -m pytest
# py.test
# py.test -v
# py.test -vrxs -> show reason of skipping test
# pytest -k mult -v -> to run the tests containing mult as substring in their name
# pytest -m two -v -> run only test which has marker two
# pytest -m "not two" -v -> run only test which does not have marker two