# pylint: skip-file
import pandas as pandas
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

strFileName		= raw_input( 'Make sure file is in current directory and enter name of the file.\n' )
arrExcelData	= pandas.read_excel( './' + strFileName )
objAnalyzer		= SentimentIntensityAnalyzer()
to_lang="en"

for strTweet in arrExcelData['text'] :
	strTweet = strTweet.replace( '\n', ' ' )
	strTweet = strTweet.replace( ',', ' ' )
	b = TextBlob(strTweet)
	from_lang=b.detect_language()
	if(from_lang=='ar'):
		tt=TextBlob(strTweet)
		strTweet=tt.translate(to="en")
		strTweet =  str(strTweet)
	vs = objAnalyzer.polarity_scores(strTweet)
	print str(vs)