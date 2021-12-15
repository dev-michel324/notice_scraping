from bs4 import BeautifulSoup as Soup
import requests

html = requests.get(url="https://redecanais.wf/").text

soup = Soup(html, "lxml")

section_main = soup.find("div", class_="col-md-12")
section_name = section_main.h2.text

movies_main = section_main.find_all("h3")

filmes = []
links = []
for movie_name in movies_main:
    filmes.append(movie_name.a.text)
    links.append(movie_name.a['href'])

images = []
movies_main = section_main.find_all("img", class_="img-responsive")
for movie_img in movies_main:
    images.append(movie_img['data-echo'])

for i in range(len(filmes)):
    print(
        f'''
            {filmes[i]}
            {links[i]}
            {images[i]}
            \n
        '''
    )