# Generated by Django 3.0.4 on 2021-07-04 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Grad', 'verbose_name_plural': 'Gradovi'},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'ordering': ['name'], 'verbose_name': 'Županija', 'verbose_name_plural': 'Županije'},
        ),
    ]
