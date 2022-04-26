from django.contrib import admin
from .models import Category, Sub_Category, Author, Course, Data_sheet, Book

# Register your models here.

@admin.register (Category)
class Category_Admin (admin.ModelAdmin):
    fields = ['name_category', ('created', 'updated')]
    list_display = ('id_category', 'name_category', 'created', 'updated')
    ordering = ['-name_category']
    list_filter = ('name_category',)
    search_fileds = 'name_category'
    readonly_fields = ('created', 'updated')



@admin.register (Sub_Category)
class Subcategory_Admin (admin.ModelAdmin):
    fields = ['name_subcategory', 'category']
    list_display = ('id_sub_category', 'name_subcategory', 'category', 'created', 'updated')
    list_display_links = ('category',)
    list_editable = ('name_subcategory',)
    list_filter = ('name_subcategory', 'category')
    date_hierarchy = 'created'
    search_fields = ('name_subcategory',)
    readonly_fields = ('created', 'updated')
    raw_id_fields = ('category',)

    ordering = ['-name_subcategory']

@admin.register(Author)
class Author_Admin (admin.ModelAdmin):
    fields = [('name_author', 'last_name'), 'sex']
    list_display = ('id_author', 'name_author', 'last_name', 'sex', 'created', 'updated')
    list_filter = ('name_author', 'last_name', 'sex')
    search_fields = ('name_author',)
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    radio_fields = {'sex': admin.HORIZONTAL}

    ordering = ['-name_author']



@admin.register (Course)
class Course_Admin (admin.ModelAdmin):
    fields = ['title_cours', 'description_cours', ('author_cours', 'image_cours'), 'subcategory', 'link_cours', 'idiom_cours']
    list_display = ('id', 'title_cours', 'description_cours', 'image_cours', 'link_cours', 'idiom_cours', 'created', 'updated')
    list_display_links = ('link_cours',)
    list_editable = ('title_cours', 'description_cours')
    list_filter = ('author_cours', 'subcategory', 'idiom_cours')
    date_hierarchy = 'created'
    search_fields = ('title', 'idiom_cours')
    readonly_fields = ('created', 'updated')

    ordering = ['-title_cours']


@admin.register (Data_sheet)
class DataShett_Admin (admin.ModelAdmin):
    fields = ['editor', ('idiom', 'size', 'year')]
    list_display = ('id', 'editor', 'idiom', 'size', 'year')
    list_editable = ('size', 'year', 'idiom')
    list_filter = ('editor', 'idiom', 'year')
    search_fields = ('editor',)



@admin.register (Book)
class Book_Admin (admin.ModelAdmin):
    fields = ['title_book', ('description_book', 'content_book'), ('author_book', 'data_sheet', 'image_book'), ('link_book', 'subcategory'), ('created', 'updated')]
    list_display = ('id','title_book', 'description_book', 'content_book', 'author_book', 'data_sheet', 'image_book', 'link_book', 'subcategory', 'created', 'updated')
    list_display_links = ('link_book',)
    list_editable = ['title_book', 'image_book']
    list_filter = ('author_book', 'subcategory',)
    date_hierarchy = 'created'
    search_fields = ('title_book', 'author_book')
    readonly_fields = ('created', 'updated')
