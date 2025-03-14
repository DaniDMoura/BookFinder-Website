from django.urls import path
from .views import Home, About, BookView, Search

urlpatterns = [
    path("",Home.as_view(), name= "home"),
    path("about/",About.as_view(), name= "about"),
    path("books/",BookView.as_view(), name= "books"),
    path("search/",Search.as_view(), name= "search"),
]
