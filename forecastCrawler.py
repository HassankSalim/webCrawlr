import re
import urllib.request
from bs4 import BeautifulSoup

city = input('Enter Ur City\n')
url = 'http://www.weather-forecast.com/locations/'+city+'/forecasts/latest'

data = urllib.request.urlopen(url).read()
dataDecode = data.decode("utf-8")

soup = BeautifulSoup(dataDecode, "html.parser")
print(dataDecode)
#print(soup.prettify())
mat = re.search(r'<span class="phrase">([^<]+)</span>', dataDecode)
print(mat.group())