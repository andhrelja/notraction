# Generated by Django 3.0.4 on 2021-07-04 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0005_auto_20210703_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'Vozač', 'verbose_name_plural': 'Vozači'},
        ),
    ]
