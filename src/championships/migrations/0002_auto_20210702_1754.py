# Generated by Django 3.0.4 on 2021-07-02 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('championships', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='championship',
            name='club_count',
        ),
        migrations.RemoveField(
            model_name='championship',
            name='club_position',
        ),
    ]
