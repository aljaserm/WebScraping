from urllib.request import urlopen
from bs4 import BeautifulSoup

# htmlData=urlopen('http://www.google.com')
# print(htmlData.read())


htmlData=urlopen('http://www.bbc.com')
bsObj=BeautifulSoup(htmlData.read(),'html.parser')
print(bsObj.h1)
print(bsObj.h1.string)
