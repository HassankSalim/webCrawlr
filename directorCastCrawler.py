#reedlin casting scraper
#bot : reedlinbot

import re
import urllib.request
import sys

file = open('director.txt', 'a')
link = 'https://en.wikipedia.org/w/index.php?title=Category:American_film_directors&pagefrom=Malick%2C+Terrence%0ATerrence+Malick#mw-pages'
wikiBaseUrl = 'https://en.wikipedia.org'
pageCounter = 2596

def scrapCurrentLink():
	global pageCounter
	req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
	data = urllib.request.urlopen(req).read()
	decodedData = data.decode('utf-8')

	#pattern for director name example:<li><a href="/wiki/Al_Adamson" title="Al Adamson">Al Adamson</a></li>
	pattern = r'<li><a href="([^"]+)" title="([^:"]+)">.+</a></li>'
	directorList = re.findall(pattern, decodedData)
	pageCounter += len(directorList)

	for i in directorList:
		requestUrl = wikiBaseUrl + i[0]
		directorName = i[1]
		storeDirectorNameAndImg(requestUrl, directorName)

	return decodedData	

def storeDirectorNameAndImg(requestUrl, directorName):
	req = urllib.request.Request(requestUrl)
	data = urllib.request.urlopen(req).read()
	decodedData = data.decode('utf-8')

	#pattern for giving image link
	#<img alt="Rosanna Arquette - Monte-Carlo Television Festival.JPG" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Rosanna_Arquette_-_Monte-Carlo_Television_Festival.JPG/220px-Rosanna_Arquette_-_Monte-Carlo_Television_Festival.JPG" width="220" height="293" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Rosanna_Arquette_-_Monte-Carlo_Television_Festival.JPG/330px-Rosanna_Arquette_-_Monte-Carlo_Television_Festival.JPG 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Rosanna_Arquette_-_Monte-Carlo_Television_Festival.JPG/440px-Rosanna_Arquette_-_Monte-Carlo_Television_Festival.JPG 2x" data-file-width="3000" data-file-height="4000" />
	pattern = r'<img alt=".*%s[^"]+" src="([^"]+)"[^>]+>'%directorName
	match = re.search(pattern, decodedData)
	if match:
		file.write('https:' + match.group(1) + '||' + directorName+'\n')
	else:
		file.write('http://www.whereincity.com/images/no-photos.jpg'+'||'+directorName+'\n')

def getNextPageLink(decodedData):
	#pattern for finding link to next page
	#<a href="/w/index.php?title=Category:American_film_directors&amp;pagefrom=Baldwin%2C+Ruth+Ann%0ARuth+Ann+Baldwin#mw-pages" title="Category:American film directors">next page</a>
	pattern = r'<a href="([^"]+)"[^>]+>next page</a>'
	match = re.search(pattern, decodedData)
	if match:
		string = match.group(1)
		string = string.replace('amp;', '')
		return wikiBaseUrl + string
	return match	


def main():
	global link
	decodedData = scrapCurrentLink()
	print('No of Completed Directors:', pageCounter)
	link = getNextPageLink(decodedData)
	print('Next link: ', link)
	if link:
		main()
	sys.exit(0)	

if __name__ == '__main__':
	main()