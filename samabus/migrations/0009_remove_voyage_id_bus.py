# Generated by Django 3.1.5 on 2021-03-16 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samabus', '0008_auto_20210316_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voyage',
            name='id_bus',
        ),
    ]