# Generated by Django 4.2.7 on 2024-09-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotativo', '0003_rename_asociadororativo_asociadorotativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escenarios',
            name='salarioMax',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]