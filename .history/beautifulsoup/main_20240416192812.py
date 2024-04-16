from bs4 import BeautifulSoup
import lxml
import requests
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


'''
FAQ: Empire's website has changed!

When this lesson was created, I used this URL for the project: 
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

However, Empire has since changed their website. You can see this when you inspect the movie title elements. 
You'll see that the h3 with the class "title" is no longer there. 
To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.

'''


with open('website.html',encoding='utf-8') as file:
    contents=file.read() # this is markup
# soup =BeautifulSoup(contents,'html.parser')
soup =BeautifulSoup(contents,'lxml')

# print(soup.title) #title tag
# print(soup.title.name) # the name of tag
# print(soup.title.string)#the content in tag
# print(soup.prettify())#the code in html web
# print(soup.a) # first tag a


all_anchors_tags = soup.find_all(name='a') # A list of a tags in HTML
print(all_anchors_tags)
for tag in all_anchors_tags:
    print(tag.getText())
    # tag.get('attribute in html')
    print(tag.get('href'))



heading = soup.find_all(name='h1',id='name' )
print(heading)

section_heading = soup.find_all(name='h3',class_='heading') # Rememberr class_ not class
print(section_heading)

company_url = soup.select_one(selector='p a') # Select a element into p element tag
print(company_url)

headings = soup.select(".heading")
print(headings)