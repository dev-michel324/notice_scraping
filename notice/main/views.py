from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

from .models import Notice

class get_news():
    links = {
        1: 'https://www.bbc.com/portuguese/topics/c404v027pd4t', #technology
        2: 'https://www.bbc.com/portuguese/topics/cr50y580rjxt', #science
        3: 'https://www.bbc.com/portuguese/topics/cvjp2jr0k9rt', #economy
        4: 'https://www.bbc.com/portuguese/topics/c340q430z4vt', #health
    }
    categorys = {1: 'technology', 2: 'science', 3: 'economy', 4: 'health'}

    def get_all(self, category: int):
        page = requests.get(url=self.links[category]).text
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
            exist = Notice.objects.filter(title=titulo[i]).exists()
            if not exist:
                new = Notice(
                    category=self.categorys[category],
                    title=titulo[i],
                    description=descricao[i],
                    date_post=data[i],
                    image=image_link[i],
                )
                new.save()

def index(request):
    news = get_news()
    for i in range(4):
        news.get_all(i+1)

    technology = Notice.objects.filter(category='technology').order_by('-date')
    science = Notice.objects.filter(category='science').order_by('-date')
    economy = Notice.objects.filter(category='economy').order_by('-date')
    health = Notice.objects.filter(category='health').order_by('-date')

    return render(request, 'main/index.html', {
        'technology': technology,
        'science': science,
        'economy': economy,
        'health': health,
    })

def page_per_category(request, category: int):
    categorys = {1: 'technology', 2: 'science', 3: 'economy', 4: 'health'}
    update = get_news()
    update.get_all(category=category)
    news = Notice.objects.filter(category=categorys[category]).order_by('-date')

    return render(request, 'main/category.html', {'news': news, 'category': categorys[category]})