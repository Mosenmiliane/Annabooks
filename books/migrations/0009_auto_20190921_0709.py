# Generated by Django 2.2.2 on 2019-09-21 00:09

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_book_original_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='biography',
            field=tinymce.models.HTMLField(default="Author's biography"),
        ),
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.FileField(blank=True, upload_to='author_img/'),
        ),
    ]