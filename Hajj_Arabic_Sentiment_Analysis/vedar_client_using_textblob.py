# pylint: skip-file
import sys
import os.path
import pandas as pandas
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

strToLanguage	= 'en'
objAnalyzer		= SentimentIntensityAnalyzer()

strFileName		= raw_input( 'Make sure file is in current directory and enter name of the file.\n' )

if( False == os.path.isfile( './' + strFileName ) ) :
	print 'No such file'
	sys.exit()

arrExcelData	= pandas.read_excel( './' + strFileName )


for strTweet in arrExcelData['text'] :
	strTweet = strTweet.replace( '\n', ' ' )
	strTweet = strTweet.replace( ',', ' ' )
	objTextBlob = TextBlob( strTweet )
	strFromLanguage = objTextBlob.detect_language()
	if( 'ar' == strFromLanguage ):
		strTweet = objTextBlob.translate( to = 'en' )
		strTweet = str( strTweet )
	objVaderAnalysis = objAnalyzer.polarity_scores(strTweet)
	print strTweet
	print str( objVaderAnalysis )