from django.urls import path
from .views import Home, About, BookView, Search, Book

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('books/', BookView.as_view(), name='books'),
    path('search/', Search.as_view(), name='search'),
    path('book/<str:id>', Book.as_view(), name='book'),
]
