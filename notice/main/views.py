from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

from .models import Notice

# Create your views here.
def get_all_news():
    categorys = ['technology']

    page = requests.get(url='https://www.bbc.com/portuguese/topics/c404v027pd4t').text
    soup = BeautifulSoup(page, 'lxml')

    title = soup.find_all('span', class_='lx-stream-post__header-text')
    titulo = []
    for i in title:
        titulo.append(i.text)
    
    description = soup.find_all('p', class_='lx-stream-related-story--summary')
    descricao = []
    for i in description:
        descricao.append(i.text)

    date = soup.find_all('span', class_='qa-post-auto-meta')
    data = []
    for i in date:
        data.append(i.text)

    image = soup.find_all('img', class_='lx-stream-related-story--index-image')
    image_link = []
    for i in image:
        image_link.append(i['src'])

    for i in range(len(titulo)):
        exist = Notice.objects.filter(title=titulo[i]).exists
        if not exist:
            new = Notice(
                category=categorys[0],
                title=titulo[i],
                description=descricao[i],
                date_post=data[i],
                image=image_link[i],
            )
            new.save()


def index(request):
    get_all_news()
    news = Notice.objects.all().order_by('-date')
    # Reserved.objects.filter(client=client_id).order_by('-check_in')
    return render(request, 'main/index.html', {'news': news})