from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.CharField(max_length=10)
    description = models.TextField()
    page_count = models.IntegerField()
    image_link = models.CharField(max_length=500)
    buy_link = models.CharField(max_length=500)
    book_id = models.CharField(max_length=100)
    is_saved = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.title} | {self.author}'