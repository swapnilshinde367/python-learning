import os

# print( os.getcwd())

os.chdir( '../' )

# print( os.getcwd())

os.chdir( 'python-learning' )

# works as ls
# print( os.listdir())

# os.rmdir( 'testdir' )
# os.mkdir( 'testdir' )

# os.removedirs( 'testdir1/subdir1/subdir2' )
# os.makedirs( 'testdir1/subdir1/subdir2' )

# os.rename( 'test.txt', 'rename.txt' )

# print( os.stat( 'rename.txt' ).st_size )

# for dirpath, dirname, filename in os.walk( '../python_test' ) :
# 	print( '{} -> {} ->, {}'.format( dirpath, dirname, filename) )

# Print all OS' environment variables os.environ
print(os.environ.get( 'HOME' ))

# safe to use os.path to avoid any extra slashes
print( os.path.join( os.environ.get( 'HOME' ), 'test.txt' ) )

# get filename from path
print( os.path.basename( '/tmp/test.txt' ) )

# get dirctory from path
print( os.path.dirname( '/tmp/test.txt' ) )

# Print split path and filename
print( os.path.split( '/tmp/test.txt' ) )

# Print split path and extension
print( os.path.splitext( '/tmp/test.txt' ) )

# Check if path exists
print( os.path.exists( '/tmp/test.txt' ) )

# If is Dir
print( os.path.isdir( 'C:\\Users\\SWAPNI~1.SHI\\AppData\\Local\\Temp' ) )

# If is File
print( os.path.isfile( '/tmp/test.txt' ) )

