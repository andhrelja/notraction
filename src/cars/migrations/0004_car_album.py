# Generated by Django 3.0.4 on 2021-07-01 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
        ('cars', '0003_auto_20210701_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='album',
            field=models.ManyToManyField(to='gallery.Gallery', verbose_name='Galerija'),
        ),
    ]