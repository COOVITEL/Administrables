# Generated by Django 4.2.5 on 2024-12-17 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_registrosimulacionescdat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrossimulacionescreditos',
            name='seniority',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrossimulacionescreditos',
            name='typeContract',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
