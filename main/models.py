from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField('Название', max_length=50)

    anons = models.CharField('Анонс', max_length=250)

    full_text = models.TextField('Статья')

    date = models.DateTimeField('Дата публикации')

    def str(self):
        return self.title


class Command(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
