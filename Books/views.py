from django.shortcuts import render
from django.views import View
import os
from dotenv import load_dotenv
from http import HTTPStatus
import requests

load_dotenv()
api_key = os.getenv('API_KEY')


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class BookView(View):
    def get(self, request):
        return render(request, 'books.html')


class Search(View):
    def get(self, request):
        query = request.GET.get('q', '')

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
                return render(request, 'search.html', {'data': books_detailed})
        return render(request, 'home.html')


class Book(View):
    def get(self, request, id):
        book = []
        response = requests.get(
            f'https://www.googleapis.com/books/v1/volumes/{id}'
        )
        data = response.json()

        info = data.get('volumeInfo', {})
        sale_info = data.get('saleInfo', {})

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
                'description': Description.strip(),
                'page_count': PageCount,
                'buy_link': BuyLink,
            }
        )

        return render(request, 'book.html', {'data': book})
