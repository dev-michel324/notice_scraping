from django import urls
from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index_page'),
    path('category/<int:category>', views.page_per_category, name='category_list'),
]