# pylint: skip-file
# Open a folder and rename the files.
# For loop for a simple array
# Rename a file in the folder

import os
def handleRenameFiles():
    os.chdir( 'secret_messages' )
    arrmixFileNames = os.listdir('./')

    for strFileName in arrmixFileNames :

        print 'Old name was ' + strFileName
        print 'New name is ' + strFileName.translate( None, '0123456789' )
        os.rename( strFileName, strFileName.translate( None, '0123456789' ) ) # Need to add range instead of numbers. 
        
    # os.chdir( '../' ) # not needed, however added
# end of handleRenameFiles this is not necessary


handleRenameFiles()