from django.db import models

class LOL(models.Model):
    name = models.CharField('название команды', max_length=200)
    namecommand = models.CharField('Команда', max_length=200)
    game = models.CharField('Игра', max_length=200)


