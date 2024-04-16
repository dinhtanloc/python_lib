from bs4 import BeautifulSoup
import lxml

with open('website.html',encoding='utf-8') as file:
    contents=file.read() # this is markup
# soup =BeautifulSoup(contents,'html.parser')
soup =BeautifulSoup(contents,'lxml')
print(soup.title) #title tag
print(soup.title.name) # the name of tag
print(soup.title.string)