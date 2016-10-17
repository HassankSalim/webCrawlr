import re
import urllib.request

url = 'http://www.dictionary.com/browse/'

try:
	word = input('Enter the Word\n')
	url = url + word

	data = urllib.request.urlopen(url).read()
	dataDecode = data.decode("utf-8")

	mat = re.search(r'<meta name="description" content="(.*).See', dataDecode)
	print(mat.group(1))
except AttributeError:
	print('Not found in Dictionary')
except urllib.error.HTTPError:		
	print('Not found in Dictionary')

