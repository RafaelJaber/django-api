from django.db import models
from django.contrib.auth.models import User


class Assessment(models.Model):
    GOOD = 3
    AVERAGE = 2
    BAD = 1
    NEUTRAL = 0

    VALUATION = (
        (GOOD, 'Boa'),
        (AVERAGE, 'Média'),
        (BAD, 'Ruim'),
        (NEUTRAL, 'Neutra')
    )

    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comentário')
    valuation = models.IntegerField(verbose_name='Avaliação', choices=VALUATION, default=NEUTRAL)
    date = models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)

    def __str__(self):
        return self.user.username + ' ' + str(self.date)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
