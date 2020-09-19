from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# class Author(models.Model):
#     nick_name = models.CharField(max_length=50)


class Genre(models.Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title


class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField(
        max_length=50,
        verbose_name='Название',
        help_text='введите название книги',
        db_index=True,
        unique=True
    )
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    text = models.TextField(verbose_name='текст')
    author = models.ManyToManyField(User, verbose_name="автор", db_index=True)
    publish_date = models.DateField(auto_now_add=True)
    genre = models.ManyToManyField('managebook.Genre', verbose_name='жанр')
    rate = models.ManyToManyField(User, through='managebook.BookLike', related_name='rate')

    def __str__(self):
        return self.title if self.title is not None else 'name is not defined'


class Comment(models.Model):
    text = models.TextField(verbose_name="текст")
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="книга")
    like = models.ManyToManyField(User, related_name='like')


class BookLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)
