from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):    
    return HttpResponse('Заглавная страница новой социальной сети для блогеров')


def group_posts(request, slug):
    return HttpResponse(f'Список постов, отфильтрованных по группам {slug}')
