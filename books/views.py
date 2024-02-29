from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import book
# Create your views here.


class BookListView(ListView):
    
    model = book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    
    model = book
    content_object_name = 'book'
    template_name = 'books/book_detail.html'