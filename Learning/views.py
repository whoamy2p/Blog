from email import message
from django.shortcuts import render, redirect
from .models import Course, Sub_Category, Book
from math import ceil

# Create your views here.

SUBCTG_COURS = Sub_Category.objects.filter (category__name_category__startswith = 'Cours')
SUBCTG_BOOKS = Sub_Category.objects.filter (category__name_category__startswith = 'Books')
cantidad = 0

def cours (request):
    global post_news
    cours = Course.objects.all ().order_by ('-id')
    post_news = cours[:4]
    cantidad_grupos = ceil (len(cours)/9)

    var = lista_p (cantidad_grupos, cours)
    sub_var = iter (var) 

    # num = 0
    if request.GET:
        num = int(request.GET['p'])
        if isinstance (num, int):
            cours = Course.objects.filter (title_cours__in=var[num])

            return render (request, 'Learning/cours/cours.html', {'cours_all': cours,'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS, 'cantidad_group': cantidad_grupos, 'range': range (cantidad_grupos)})

    cours = Course.objects.filter (title_cours__in=next (sub_var))

    return render (request, 'Learning/cours/cours.html', {'cours_all': cours,'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS, 'cantidad_group': cantidad_grupos, 'range': range (cantidad_grupos), 'post': post_news})


# funcion iteradora de cursos
def lista_p (cant_group, cours):
    new_lista = []
    inicio, fin = 0, 9
    for k in range (cant_group):
        new_lista.append(list(cours[inicio:fin]))
        inicio, fin = fin, fin+9

    return new_lista
# aqui vamos a mostras los opst nuevos de la subcategora

def subcategory_cours (request, name_subctg):
    cours = Course.objects.filter (subcategory__name_subcategory=name_subctg).order_by ('-id')
    try:
        post_news = cours[:4]
    except IndexError as it:
        print ('fallo en indice de cursos')

    cantidad_grupos = ceil (len(cours)/9)
    var = lista_p (cantidad_grupos, cours)
    if request.GET:
        num = int (request.GET['p'])
        if isinstance (num, int):
            cours = Course.objects.filter (title_cours__in=var[num])

            return render (request, 'Learning/cours/subcategory_cours.html', {'cours_all': cours, 'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS, 'name_subctg': name_subctg, 'range': range (cantidad_grupos), 'post': post_news})

    cours = Course.objects.filter (title_cours__in=var[0])

    return render (request, 'Learning/cours/subcategory_cours.html', {'cours_all': cours, 'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS, 'name_subctg': name_subctg, 'range': range (cantidad_grupos), 'post': post_news})

# seccion de vista de libros

def books (request):
    book = Book.objects.all ().order_by ('-id')
    post_news = book[:4]
    cantidad_grupos = ceil (len(book)/9)

    var = lista_p (cantidad_grupos, book)

    # num = 0
    if request.GET:
        num = int(request.GET['p'])
        if isinstance (num, int):
            book = Course.objects.filter (title_cours__in=var[num])

            return render (request, 'Learning/books/books.html', {'books_all': book,'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS, 'range': range(cantidad_grupos)})

    book = Book.objects.filter (title_book__in=var[0])

    return render (request, 'Learning/books/books.html', {'books_all': book,'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS, 'range': range(cantidad_grupos), 'post': post_news})


def subcategory_books (request, name_subctg):
    book = Book.objects.filter (subcategory__name_subcategory=name_subctg).order_by ('-id')
    post_news = book[:4]
    cantidad_grupos = ceil (len(book)/9)

    var = lista_p (cantidad_grupos, book)

    if request.GET:
        num = int(request.GET['p'])
        if isinstance (num, int):
            book = Course.objects.filter (title_cours__in=var[num])

            return render (request, 'Learning/books/subcategory_books.html', {'books_all': book, 'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS, 'name_subctg': name_subctg, 'range': range(cantidad_grupos), 'post': post_news})

    try:
        book = Book.objects.filter (title_book__in=var[0])
    except IndexError as It:
        book = 'never'

    return render (request, 'Learning/books/subcategory_books.html', {'books_all': book, 'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS, 'name_subctg': name_subctg, 'range': range(cantidad_grupos), 'post': post_news})