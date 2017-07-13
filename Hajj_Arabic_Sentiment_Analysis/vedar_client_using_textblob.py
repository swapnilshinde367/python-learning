# pylint: skip-file
import sys
import os.path
import pandas as pandas
import mysql.connector
from textblob import TextBlob
from mysql.connector import Error
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

strToLanguage		= 'en'
objAnalyzer			= SentimentIntensityAnalyzer()
arrmixDataToInsert	= []

objMysqlConnection	= mysql.connector.connect(	host		= 'localhost',
												database	= 'db_name',
												user		= 'root',
												password	= 'password' )

strFileName			= raw_input( 'Make sure file is in current directory and enter name of the file.\n' )

if( False == os.path.isfile( './' + strFileName ) ) :
	print 'No such file'
	sys.exit()

arrmixExcelData	= pandas.read_excel( './' + strFileName )

for intIndex in range( len( arrmixExcelData['text'] ) ) :

	strOriginalTweet	= arrmixExcelData['text'][intIndex]
	strUserName			= arrmixExcelData['user_full_name'][intIndex]

	if ( type( strUserName ) is not unicode and type( strUserName ) is not str )  :
		strUserName = 'NA'

	strOriginalTweet	= strOriginalTweet.replace( '\n', ' ' )
	strOriginalTweet	= strOriginalTweet.replace( ',', ' ' )
	strTranslatedTweet	= strOriginalTweet

	objTextBlob			= TextBlob( strOriginalTweet )
	strFromLanguage		= objTextBlob.detect_language()

	if( 'ar' == strFromLanguage ):
		strTranslatedTweet = objTextBlob.translate( to = 'en' )
		strTranslatedTweet = str( strTranslatedTweet )

	objVaderAnalysis = objAnalyzer.polarity_scores( strTranslatedTweet )
	intScore = 0

	if( 0.5 <= objVaderAnalysis['pos'] ) :
		intScore = 1
	elif( 0.5 <= objVaderAnalysis['neg'] ) :
		intScore = -1

	arrmixTweetData = ( strUserName,
						strOriginalTweet,
						strTranslatedTweet,
						intScore,
						objVaderAnalysis['pos'],
						objVaderAnalysis['neg'],
						objVaderAnalysis['neu'] )

	arrmixDataToInsert.append( arrmixTweetData )

strQuery = 'INSERT INTO `twitter_sentiment_analysis` \
(`user_name`, \
`original_tweet`, \
`translated_tweet`, \
`score`, \
`positive`, \
`negative`, \
`neutral`) \
VALUES \
(%s,%s,%s,%s,%s,%s,%s)'

objCursor = objMysqlConnection.cursor()
objCursor.executemany( strQuery, arrmixDataToInsert )
objMysqlConnection.commit()