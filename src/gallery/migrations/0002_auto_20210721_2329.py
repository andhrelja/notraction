# Generated by Django 3.0.4 on 2021-07-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='images',
            field=models.ManyToManyField(blank=True, to='gallery.Image', verbose_name='Slike'),
        ),
    ]
