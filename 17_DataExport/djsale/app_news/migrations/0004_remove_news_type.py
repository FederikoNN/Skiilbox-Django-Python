# Generated by Django 4.0.6 on 2022-08-07 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_alter_news_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='type',
        ),
    ]
