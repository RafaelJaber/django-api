from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comentário')
    date = models.DateField(auto_now_add=True, verbose_name='Data de Criação')
    status = models.BooleanField(default=False, verbose_name='Aprovado')

    def __str__(self):
        return self.user.username + ' ' + str(self.date)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
