# Generated by Django 5.1.7 on 2025-03-17 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0005_rename_borrower_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='buy_link',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='image_link',
            field=models.CharField(max_length=500),
        ),
    ]
