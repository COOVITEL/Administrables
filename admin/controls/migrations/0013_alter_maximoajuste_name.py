# Generated by Django 4.2.5 on 2024-07-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0012_maximoajuste_delete_maximoajusteaporte_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maximoajuste',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
