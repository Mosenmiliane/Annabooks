# Generated by Django 2.2.2 on 2019-09-03 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20190903_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FileField(blank=True, upload_to='book_img/'),
        ),
    ]