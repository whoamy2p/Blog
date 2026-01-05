from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    id_category = models.AutoField (primary_key=True, unique=True)
    name_category = models.CharField (max_length=40, unique=True)

    created = models.DateField (auto_now_add=True)
    updated = models.DateField (auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__ (self):
        return self.name_category


class Sub_Category (models.Model):
    id_sub_category = models.AutoField (primary_key=True, unique=True, null=False)
    name_subcategory = models.CharField (max_length=50, unique=True)
    category = models.ForeignKey (Category, on_delete=models.CASCADE)

    created = models.DateField (auto_now_add=True)
    updated = models.DateField (auto_now_add=True)
    
    class Meta:
        verbose_name = 'Sub_Category'
        verbose_name_plural = 'Sub_Categories'

    def __str__ (self):
        return self.name_subcategory


class Author (models.Model):
    GENDER = [('M', 'Men'), ('F', 'Women'), ('O', 'Others')]
    id_author = models.AutoField (primary_key=True, unique=True)
    name_author = models.CharField (max_length=40)
    last_name = models.CharField (max_length=50)
    sex = models.CharField (choices=GENDER, max_length=20)

    created = models.DateField (auto_now_add=True)
    updated = models.DateField (auto_now_add=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__ (self):
        return '%s %s'%(self.name_author, self.last_name)
        

class Course (models.Model):
    title_cours = models.CharField (max_length=400, unique=True)
    description_cours = models.TextField ()
    author_cours = models.ManyToManyField (Author)
    image_cours = models.ImageField (upload_to = 'learning')
    subcategory = models.ManyToManyField (Sub_Category)
    link_cours = models.URLField ()
    rating = models.IntegerField(default=5)
    idiom_cours = models.CharField (max_length=20, blank=True, null=True)
    # auth_admin = models.ForeignKey (User, on_delete=models.CASCADE)

    created = models.DateField (auto_now_add=True)
    updated = models.DateField (auto_now_add=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['title_cours']

    def __str__ (self):
        return self.title_cours

# crear una clase de datos del editor
class Data_sheet (models.Model):
    editor = models.CharField (max_length=100, blank=True, null=True)
    idiom = models.CharField (max_length=30, blank=True, null=True)
    size = models.TextField (default='0 kb', blank=True, null=True)
    year = models.IntegerField (default=2022, blank=True, null=True)

    def __str__ (self):
        return self.editor


class Book (models.Model):
    title_book = models.CharField (max_length=250, unique=True)
    description_book = models.TextField ()
    content_book = models.TextField ()
    author_book = models.ForeignKey (Author, on_delete=models.CASCADE)
    # cambiar a ManyToManyField no (OneToOneField)
    data_sheet = models.OneToOneField (Data_sheet, on_delete=models.CASCADE)
    image_book = models.ImageField (upload_to = 'learning')
    link_book = models.URLField ()
    rating = models.IntegerField(default=5)

    subcategory = models.ForeignKey (Sub_Category, on_delete=models.CASCADE)

    created = models.DateField (auto_now_add=True)
    updated = models.DateField (auto_now_add=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__ (self):
        return self.title_book

# crear un clase de promociones de imagens enlasado a su respectivo subcategori

