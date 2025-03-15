from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.DateField()
    description = models.TextField()
    page_count = models.IntegerField()
    language = models.CharField(max_length=255)
    image_link = models.CharField()
    buy_link = models.CharField()


def __str__(self):
    return f'{self.title} | {self.author}'
