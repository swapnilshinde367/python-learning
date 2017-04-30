# pylint: skip-file
# open a file
# open a check profanity in it using wdyl site using urllib

import urllib

def handleCheckProfanityInFile() :

    objFile = open( './Text_Files/movie_quotes.txt' )
    strContent = objFile.read()
    
    objFile.close()

    objConnection = urllib.urlopen( 'http://www.wdylike.appspot.com/?q=' + strContent )

    strOutput = objConnection.read()

    if 'true' in strOutput:
        print( 'Profanity Alert!!' )
    else:
        print( 'All OK!' )

handleCheckProfanityInFile()