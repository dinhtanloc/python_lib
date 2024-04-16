from bs4 import BeautifulSoup
import requests


def scrapping_data(url,tag,attr,cls=None,id=None,storage=[],mode=None):
    response = requests.get(url) #get data from url website
    contents = response.text # It is the same like a content when use open to open file html
    soup = BeautifulSoup(contents, 'html.parser')
    for article_tag in soup.find_all(name=tag, class_=cls):
        if mode=='text':
            storage.append(article_tag.getText())
        # article_links.append(article_tag.find("a")["href"])
        elif mode=='link':
            storage.append(article_tag.find('a').get('href'))
        # ....... code your logic here

    return storage

