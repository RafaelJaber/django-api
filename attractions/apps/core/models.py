from django.db import models
from attractions.apps.attraction.models import Attraction
from attractions.apps.comments.models import Comment
from attractions.apps.assessments.models import Assessment
from attractions.apps.addresses.models import Address


class TouristSpot(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=150)
    description = models.TextField(verbose_name='Descrição')
    status = models.BooleanField(verbose_name='Aprovado', default=False)
    attractions = models.ManyToManyField(Attraction, verbose_name='Atrações')
    comment = models.ManyToManyField(Comment, verbose_name='Comentários', blank=True)
    assessment = models.ManyToManyField(Assessment, verbose_name='Avaliações', blank=True)
    address = models.ForeignKey(Address, verbose_name='Endereço', on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='spots', null=True, blank=True)

    @property
    def full_description_2(self):
        return '%s - %s - 2' % (self.name, self.description)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ponto Turístico'
        verbose_name_plural = 'Pontos Turísticos'
        ordering = ['name']
