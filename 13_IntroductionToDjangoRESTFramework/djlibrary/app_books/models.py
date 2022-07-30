from django.db import models


class Author(models.Model):
    """Модель автора"""
    first_name = models.CharField(max_length=20, verbose_name='first_name')
    last_name = models.CharField(max_length=30, verbose_name='last_name')
    birth_year = models.IntegerField(verbose_name='birth_year')
    # books = models.ManyToManyField('Book', blank=True, verbose_name='books')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class Book(models.Model):
    """Модель книги"""
    title = models.CharField(max_length=50, verbose_name='title')
    isbn = models.CharField(max_length=20, verbose_name='isdn')
    edition_year = models.IntegerField(verbose_name='edition_year')
    pages_number = models.IntegerField(default=0, verbose_name='pages_number')
    authors = models.ManyToManyField('Author', blank=True,
                                     verbose_name='authors')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
