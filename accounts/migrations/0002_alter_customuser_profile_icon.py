# Generated by Django 5.0.4 on 2024-05-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_icon',
            field=models.ImageField(blank=True, default='profile_icon/default.png', null=True, upload_to='profile_icons/'),
        ),
    ]
