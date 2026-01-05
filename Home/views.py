from django.shortcuts import render
from Learning.models import Course, Sub_Category
from .models import News

# Create your views here.

SUBCTG_COURS = Sub_Category.objects.filter (category__name_category__startswith = 'Cours')
SUBCTG_BOOKS = Sub_Category.objects.filter (category__name_category__startswith = 'Books')

def home (request):
    cours = Course.objects.all ().order_by ('-id')[:3]


    return render (request, 'Home/index.html', {'cours_all':cours, 'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS})

def news_list(request):
    news = News.objects.all()
    return render(request, 'Home/noticias.html', {
        'news_all': news, 
        'subctg_cours': SUBCTG_COURS, 
        'subctg_books': SUBCTG_BOOKS
    })

