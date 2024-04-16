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

for tag in all_anchors_tags:
    print(tag.getText())
    # tag.get('attribute in html')
    print(tag.get('href'))

heading = soup.find_all(name='h1',id='name' )
print(heading)

section_heading = soup.find_all(name='h3',class_='heading') # Rememberr class_ not class
print(section_heading.get('class_'))

company_url = soup.select_one(selector='p a')
print(company_url)