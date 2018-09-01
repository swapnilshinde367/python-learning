# pylint: skip-file
import time
import urllib
import requests
import bs4

strArticleLink	= "https://en.wikipedia.org/wiki/Special:Random"
strTargetLink	= "https://en.wikipedia.org/wiki/Philosophy"

def handleGetFirstLink( strArticleLink ) :

	print ( strArticleLink )
	response = requests.get( strArticleLink )
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	strContentDiv = soup.find(id='mw-content-text').find(class_="mw-parser-output")

	strFirstLink = None
	for strElement in strContentDiv.find_all( 'p', recursive = False ) :
		if strElement.a:
			strFirstLink = strElement.find( 'a', recursive = False ).get( 'href' )
			break;

	if not strFirstLink :
		return strFirstLink

	return  urllib.parse.urljoin( 'https://en.wikipedia.org/', strFirstLink )

for intCount in range( 1, 25 ) :

	if strArticleLink :
		strArticleLink = handleGetFirstLink( strArticleLink )
#		arrstrSearchHistory.append( strArticleLink )
#
# def handleValidateCrawling( arrstrSearchHistory, strTargetLink ) :
