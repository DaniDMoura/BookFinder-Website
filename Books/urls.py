from django.urls import path,include
from .views import Home, About, BooksView, Search, BookView, Signup

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('books/', BooksView.as_view(), name='book-list'),
    path('search/', Search.as_view(), name='search'),
    path('book/<str:id>', BookView.as_view(), name='book'),
    path('books/delete/<str:id>/', BooksView.as_view(), name='book-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', Signup.as_view(), name='signup'),
]
