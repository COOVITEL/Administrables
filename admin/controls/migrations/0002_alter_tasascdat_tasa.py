# Generated by Django 4.2.5 on 2024-07-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasascdat',
            name='tasa',
            field=models.FloatField(),
        ),
    ]