import re
from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.google.com/finance?q='
stock = input('Stock Name\n')
url = url + stock
print(url)

# url = "https://www.google.co.in/?q="
# songDetails = str(input("Song Name\n")).split()
# url = url + '+'.join(songDetails)+'+mp3+download'
# print(url)

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")

soup = BeautifulSoup(data, "html.parser")
print(soup.prettify())

mat = re.search(r'meta itemprop="price"\n.+content="(\d+\.\d+)"', data1)
print(mat.group(1))

