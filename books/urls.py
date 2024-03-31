from django.urls import path
from .views import (BookListView,
                    BookDetailView, 
                    SearchResultsListView,
                    ReadBookDetailView,)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('read_book/<uuid:pk>/', ReadBookDetailView.as_view(), name = 'read'),
]