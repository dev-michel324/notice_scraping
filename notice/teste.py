from bs4 import BeautifulSoup
import requests

page = requests.get(url='https://www.bbc.com/portuguese/topics/c404v027pd4t').text
soup = BeautifulSoup(page, 'lxml')

image = soup.find_all('img', class_='lx-stream-related-story--index-image')
image_link = []
for i in image:
	image_link.append(i['src'])
print(image_link)
