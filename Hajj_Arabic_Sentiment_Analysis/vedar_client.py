# pylint: skip-file
import csv
import json
import urllib
import requests
import pandas as pandas
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

strEndPointUrl = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170711T175802Z.3c6b4a88016ebad0.cdbc34c633022687c3a9946cc9b670a542f6ccdf&lang=ar-en'
strFileName = raw_input( 'Make sure file is in current directory and enter name of the file.\n' )
arrExcelData = pandas.read_excel( './' + strFileName )
analyzer = SentimentIntensityAnalyzer()

for strTweet in arrExcelData['text'] :
	strTweet = strTweet.replace( '\n', ' ' )
	strTweet = strTweet.replace( ',', ' ' )
	# print strTweet
	arrmixParameters = {
		'text' : strTweet
	}
	# print arrmixParameters
	objRequest = requests.post( url = strEndPointUrl, params = arrmixParameters )
	arrmixResponse = objRequest.json()
	# arrmixResponse = json.dumps( arrmixResponse )
	# arrmixResponse = json.loads( arrmixResponse )
	strTweet = arrmixResponse['text'][0]
	vs = analyzer.polarity_scores(strTweet)
	# print("{:-<65} {}".format(strTweet, str(vs)))
	print str(vs)

# analyzer = SentimentIntensityAnalyzer()
# for sentence in sentences:
#     vs = analyzer.polarity_scores(sentence)
#     print("{:-<65} {}".format(sentence, str(vs)))