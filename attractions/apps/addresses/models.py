from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=150, verbose_name='Rua')
    number = models.IntegerField(verbose_name='Número', blank=True, null=True)
    neighborhood = models.CharField(max_length=150, verbose_name='Bairro', blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name='Cidade')
    state = models.CharField(max_length=150, verbose_name='Estado')
    country = models.CharField(max_length=100, verbose_name='País')
    latitude = models.IntegerField(null=True, blank=True, verbose_name='Latitude')
    longitude = models.IntegerField(null=True, blank=True, verbose_name='Longitude')

    def __str__(self):
        return 'Rua ' + self.street + ' - ' + self.city + ' - ' + self.state + ' - ' + self.country

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
