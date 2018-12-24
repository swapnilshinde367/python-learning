from mysql_class import MySqlConn
import pytest

cur  = None
conn = None

def setup_module( module ) :
	global cur
	global conn
	db = MySqlConn()
	conn = db.connect( 'server' )
	cur = conn.cursor()

def teardown_module( module ) :
	cur.close()
	conn.close()

def test_abc_id() :
	id = cur.execute( "select id from employee where name = 'abc'" )
	assert 123 == id

def test_xyz_id() :
	id = cur.execute( "select id from employee where name = 'xyz'" )
	assert 789 == id