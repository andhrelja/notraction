# Generated by Django 3.0.4 on 2021-07-04 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0007_auto_20210705_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driversubcategoryposition',
            name='position',
            field=models.IntegerField(blank=True, null=True, verbose_name='Plasman'),
        ),
    ]
