from django.db import models


class Attraction(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=150)
    description = models.TextField(verbose_name='Descrição')
    status = models.BooleanField(verbose_name='Aprovado', default=False)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Ponto Turístico'
        verbose_name_plural = 'Pontos Turísticos'
        ordering = ['name']
