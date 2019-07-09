from django.db import models


class Attraction(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=150)
    description = models.TextField(verbose_name='Descrição')
    operating_hours = models.TextField(verbose_name='Horário de Funcionamento')
    minimum_age = models.IntegerField(verbose_name='Idade Mínima')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'
        ordering = ['name']


