# Generated by Django 5.1.7 on 2025-03-17 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0004_book_borrower'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='borrower',
            new_name='user',
        ),
    ]
