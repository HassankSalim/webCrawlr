#reedlin casting scraper
#bot : reedlinbot

import re
import urllib.request
import sys

file = open('actress.txt', 'a') 
link = 'http://www.whereincity.com/movies/hollywood/actress' #For actors link is http://www.whereincity.com/movies/hollywood/actors/

def getDetailInPage():
	req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
	data = urllib.request.urlopen(req).read()
	decodedData = data.decode("utf-8")

	#pattern of actor and their image link
	pattern = r"<img src=.(http://www.whereincity.com/files/[^']+|http://www.whereincity.com/images/no-photos.jpg).+alt=.([^\"]+).+>"
	actorsListInCurrentPage = re.findall(pattern, decodedData)
	
	#writing to file
	for i in actorsListInCurrentPage:
		string = '||'.join(i)
		file.write(string+'\n')
	return decodedData	

def getNextButtonLink(decodedData):
	#pattern for link to next page
	pattern = r"<a href='([^']+)[^>]+>Next</a>"
	match = re.search(pattern, decodedData)
	print(link)
	if not match:
		print("NoneCheck")
		return match
	print("hi : "+match.group(1))	
	return match.group(1)


def main():
	global link
	decodedData = getDetailInPage()
	link = getNextButtonLink(decodedData)
	print("link in main:"+str(link))
	if link:
		main()
	sys.exit(0)	

if __name__ == '__main__':
	main()