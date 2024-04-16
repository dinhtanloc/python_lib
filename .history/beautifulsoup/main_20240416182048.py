from bs4 import BeautifulSoup
import lxml

with open('website.html',encoding='utf-8') as file:
    contents=file.read() # this is markup
# soup =BeautifulSoup(contents,'html.parser')
soup =BeautifulSoup(contents,'lxml')

# print(soup.title) #title tag
# print(soup.title.name) # the name of tag
# print(soup.title.string)#the content in tag
# print(soup.prettify())#the code in html web
# print(soup.a) # first tag a


all_anchors_tags = soup.find_all(name='a')
print(all_anchors_tags)
