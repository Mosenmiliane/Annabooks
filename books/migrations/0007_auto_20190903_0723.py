# Generated by Django 2.2.2 on 2019-09-03 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(blank=True, upload_to='article_img/'),
        ),
    ]
