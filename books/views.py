from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import book
from django.db.models import Q
# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    
    model = book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    
    model = book
    content_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status' # new

class SearchResultsListView( ListView):
    model = book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    # queryset = book.objects.filter(title__icontains='beginners' )

    def get_queryset(self):
        query = self.request.GET.get('q')
        return (book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(price__icontains=query))) 
     