import calc
import unittest

class CTestCalc( unittest.TestCase ) :

	def test_add( self ):
		self.assertEqual( 15, calc.add( 10, 5 ) )
		self.assertEqual( 0, calc.add( -10, 10 ) )
		self.assertEqual( 5, calc.add( -10, 15 ) )

	def test_multiplication( self ):
		self.assertEqual( 50, calc.multiplication( 10, 5 ) )
		self.assertEqual( -100, calc.multiplication( -10, 10 ) )
		self.assertEqual( 150, calc.multiplication( -10, -15 ) )

	def test_divide( self ):
		self.assertEqual( 2, calc.divide( 10, 5 ) )
		self.assertEqual( 2.5, calc.divide( 25, 10 ) )
		# self.assertEqual( 2, calc.divide( 10, 0 ) )

		with self.assertRaises( ValueError ) :
			calc.divide( 10, 0 )

if __name__ == '__main__' :
	unittest.main()