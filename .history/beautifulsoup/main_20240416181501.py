from bs4 import BeautifulSoup
import lxml

with open('website.html') as file:
    contents=file.read() # this is markup
# soup =BeautifulSoup(contents,'html.parser')
soup =BeautifulSoup(contents,'lxml')
print(soup.title.name)