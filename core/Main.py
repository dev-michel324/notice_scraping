from bs4 import BeautifulSoup as Soup
import requests

html = requests.get(url="https://redecanais.wf/").text

soup = Soup(html, "lxml")

section_main = soup.find_all("div", class_="col-md-12")

for movie in section_main:
    title_link = movie.find('a', class_="ellipsis")
    img = movie.find('img', class_="img-responsive")

    print(
        f'''
            Nome: {title_link.text}
            Link: {title_link['href']}
            Img: {img['data-echo']}
        '''
    )