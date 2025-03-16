from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.CharField(max_length=10)
    description = models.TextField()
    page_count = models.IntegerField()
    image_link = models.CharField()
    buy_link = models.CharField()
    book_id = models.CharField()
    is_saved = models.BooleanField(default=True)


def __str__(self):
    return f'{self.title} | {self.author}'
