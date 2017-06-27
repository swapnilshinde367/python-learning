# pylint: skip-file
import csv
import requests
import pandas as pandas

strEndPointUrl = 'http://0.0.0.0:5000/api/?algo=sentiment140&language=auto'
arrExcelData = pandas.read_excel( './Twitter_Feed_Data.xlsx')

with open( 'test.csv', 'wb' ) as objCsvFile :
	objCsvFile.write( 'text, sentiment, polarity\n' )
# objCsvFile = csv.writer( 'test.csv' )

	for strTweet in arrExcelData['text'] :
		strTweet = strTweet.replace( '\n', ' ' )
		strTweet = strTweet.replace( ',', ' ' )
		arrmixParameters = {
			'i' : strTweet
		}
		objRequest = requests.get( url = strEndPointUrl, params = arrmixParameters )
		arrmixResponse = objRequest.json()
		arrmixSentimentData = arrmixResponse['entries'][0]['sentiments'][0]
		print arrmixSentimentData['marl:hasPolarity']
		print arrmixSentimentData['marl:polarityValue']
		objCsvFile.write( strTweet.encode('utf-8') + ',' + arrmixSentimentData['marl:hasPolarity'].encode('utf-8') + ',' + str( arrmixSentimentData['marl:polarityValue'] ).encode('utf-8') + '\n' )
		# sys.exit()

# objCsvFile.close()
