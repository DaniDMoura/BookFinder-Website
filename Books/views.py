from django.shortcuts import render,redirect
from django.views import View
import os
from dotenv import load_dotenv
from http import HTTPStatus
import requests
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

load_dotenv()
api_key = os.getenv('GOOGLE_BOOKS_API_KEY')


def get_data_with_id(id):
    book = []
    response = requests.get(
        f'https://www.googleapis.com/books/v1/volumes/{id}'
    )
    data = response.json()

    info = data.get('volumeInfo', {})
    sale_info = data.get('saleInfo', {})
    book_id = data.get('id', '')

    Title = info.get('title', 'Unknown')
    Author = ', '.join(info.get('authors', ['Unknown']))
    Publisher = info.get('publisher', 'Unknown')
    PublishedDate = info.get('publishedDate', 'Unknown')
    Image = info.get('imageLinks', {}).get('thumbnail', None)
    Description = info.get('description', '')
    PageCount = info.get('pageCount', 'Unknown')
    BuyLink = sale_info.get('buyLink', '')

    book.append(
        {
            'title': Title,
            'authors': Author,
            'publisher': Publisher,
            'published_date': PublishedDate,
            'image': Image,
            'description': Description,
            'page_count': PageCount,
            'buy_link': BuyLink,
            'id': book_id,
        }
    )
    return book


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')



class BooksView(LoginRequiredMixin, View):
    def get(self, request):
        saved_books = Book.objects.filter(user=request.user)
        books_values = list(saved_books.values('title', 'image_link', 'book_id'))
        return render(request, 'books.html', {'books': books_values})
    def post(self, request, id):
        book = Book.objects.filter(book_id=id)
        book.delete()
        return redirect('/books')



class Search(View):
    def get(self, request):
        query = request.GET.get('q', '').strip()

        if query:
            url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}&maxResults=40'
            response = requests.get(url)

            if response.status_code == HTTPStatus.OK:
                data = response.json()
                books = data.get('items', [])

                books_detailed = []
                for book in books:
                    info = book.get('volumeInfo', {})
                    book_id = book.get('id', '')

                    Title = info.get('title', 'Unknown')
                    Author = ', '.join(info.get('authors', ['Unknown']))
                    Publisher = info.get('publisher', 'Unknown')
                    PublishedDate = info.get('publishedDate', 'Unknown')
                    Image = info.get('imageLinks', {}).get('thumbnail', None)
                    books_detailed.append(
                        {
                            'title': Title,
                            'authors': Author,
                            'publisher': Publisher,
                            'published_date': PublishedDate,
                            'image': Image,
                            'id': book_id,
                        }
                    )
                return render(
                    request,
                    'search.html',
                    {'data': books_detailed, 'query': query},
                )
        return render(request, 'home.html')


class BookView(LoginRequiredMixin, View):
    def get(self, request, id):
        book = get_data_with_id(id)
        is_saved = Book.objects.filter(book_id=id)
        if is_saved:
            return render(request, 'book.html', {'data': book, 'saved':True})
        return render(request, 'book.html', {'data': book})
    def post(self, request, id):
        book = get_data_with_id(id)[0]
        book_new_object = Book.objects.create(
            title=book.get('title'),
            author=book.get('authors'),
            publisher=book.get('publisher'),
            published_date=book.get('published_date'),
            description=book.get('description'),
            page_count=book.get('page_count'),
            image_link=book.get('image'),
            buy_link=book.get('buy_link'),
            book_id=book.get('id'),
            user=request.user
        )
        book_new_object.save()
        return redirect('/books')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class Signup(View):
    def get(self,request):
        return render(request, 'signup.html',{'form':SignUpForm})
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
