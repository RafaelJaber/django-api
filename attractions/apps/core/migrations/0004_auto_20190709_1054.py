# Generated by Django 2.2.3 on 2019-07-09 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0001_initial'),
        ('comments', '0001_initial'),
        ('core', '0003_touristspot_attractions'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='assessment',
            field=models.ManyToManyField(to='assessments.Assessment', verbose_name='Avaliações'),
        ),
        migrations.AddField(
            model_name='touristspot',
            name='comment',
            field=models.ManyToManyField(to='comments.Comment', verbose_name='Comentários'),
        ),
    ]
