# Generated by Django 2.2.3 on 2019-07-09 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('core', '0004_auto_20190709_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='addresses.Address', verbose_name='Endereço'),
            preserve_default=False,
        ),
    ]
