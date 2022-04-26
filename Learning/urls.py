from django.urls import path
from . import views

urlpatterns = [
    path ('cursos/', views.cours, name="Cursos"),
    path ('cursos/<str:name_subctg>/', views.subcategory_cours, name='sub_categoria_cours'),
    path ('libros/', views.books, name="Libros"),
    path ('libros/<str:name_subctg>/', views.subcategory_books, name='sub_categoria_books'),
]

#path ('cursor/?p=<int:num>/',views.cours_p, name="P"),