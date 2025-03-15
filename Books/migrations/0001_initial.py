# Generated by Django 5.1.7 on 2025-03-14 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('published_date', models.DateField()),
                ('description', models.TextField()),
                ('page_count', models.IntegerField()),
                ('language', models.CharField(max_length=255)),
                ('image_link', models.CharField()),
                ('buy_link', models.CharField()),
            ],
        ),
    ]
