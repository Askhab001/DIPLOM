from django.db import models



class News(models.Model):
    title = models.CharField('Название', max_length=50)

    anons = models.CharField('Анонс', max_length=250)

    full_text = models.TextField('Статья')

    date = models.DateTimeField('Дата публикации')

    def str(self):
        return self.title


