# Generated by Django 5.0.4 on 2024-05-02 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='book_covers/default.png', upload_to='book_covers/'),
        ),
    ]
