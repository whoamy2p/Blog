from unicodedata import category
from django.shortcuts import render
from Learning.models import Course, Sub_Category

# Create your views here.

SUBCTG_COURS = Sub_Category.objects.filter (category__name_category__startswith = 'Cours')
SUBCTG_BOOKS = Sub_Category.objects.filter (category__name_category__startswith = 'Books')

def home (request):
    cours = Course.objects.all ().order_by ('-id')[:9]

    return render (request, 'Home/index.html', {'cours_all':cours, 'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS})

