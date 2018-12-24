import pytest
from mysql_class import MySqlConn

@pytest.fixture( scope = 'module' )
def cur() :
	# print( 'start' )
	db = MySqlConn()
	conn = db.connect( 'server' )
	cursor = conn.cursor()
	yield cursor
	cursor.close()
	conn.close()
	# print( 'end' )

def test_abc_id( cur ) :
	id = cur.execute( "select id from employee where name = 'abc'" )
	assert 123 == id

def test_xyz_id( cur ) :
	id = cur.execute( "select id from employee where name = 'xyz'" )
	assert 789 == id

# pytest -v --capture=no
