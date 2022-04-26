from urllib.parse import ParseResultBytes
from django.shortcuts import render
from .forms import FormApp
from django.views import View
from Learning.views import SUBCTG_BOOKS, SUBCTG_COURS

# Create your views here.

class Forms_contact (View):
    def get (self, request):
        form = FormApp ()

        return render (request, 'Contact/contacto.html', {'form': form, 'subctg_cours': SUBCTG_COURS, 'subctg_books': SUBCTG_BOOKS})

    def post (self, request):
        pass