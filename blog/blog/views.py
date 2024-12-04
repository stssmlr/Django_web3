from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")

def contactpage(request):
    return render(request, "contact.html")

def newspage(request):
    news_items = [
        {"title": "Новина 1", "content": "Опис першої новини."},
        {"title": "Новина 2", "content": "Опис другої новини."},
    ]
    return render(request, 'news.html', {'news_items': news_items})