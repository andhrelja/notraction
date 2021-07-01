# Generated by Django 3.1.3 on 2020-11-15 19:44

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=gallery.models.get_upload_path, verbose_name='Slika')),
                ('alt', models.CharField(max_length=50, verbose_name='Naziv')),
            ],
            options={
                'verbose_name': 'Slika',
                'verbose_name_plural': 'Slike',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Naziv')),
                ('images', models.ManyToManyField(to='gallery.Image', verbose_name='Slike')),
            ],
            options={
                'verbose_name': 'Galerija',
                'verbose_name_plural': 'Galerije',
            },
        ),
    ]