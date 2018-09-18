import time
import urllib
import requests
import bs4

strArticleLink = 'http://www.mrepc.com/marketplace/public/smg.php';

response = requests.get( strArticleLink )
html = response.text
soup = bs4.BeautifulSoup(html, "html.parser")

strContentDiv = soup.find(class_="body_textarea2")

for strElement in strContentDiv.find_all( class_="itemBox AD2 nobox2", recursive = False ) :
	if 'Manufacturer' in str(strElement) :
		strElement.find(class_="box").decompose()
		strElement.find(class_="box1").decompose()

		del strElement.find(class_="box6")['style']

		if strElement.find(class_="box4").find('h2').find('font').find('img') :
			strElement.find(class_="box4").find('h2').find('font').find('img').decompose()
		strElement.find(class_="box4").find('h2').find('strong').decompose()

		boxes = strElement.find_all(class_="box5")
		for box in boxes:
			box.decompose()

		print(str(strElement).encode('utf-8'))

# print(str(strContentDiv).encode('utf-8'))