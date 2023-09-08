# Generated by Django 4.2.4 on 2023-09-08 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TasasCDAT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('since', models.IntegerField()),
                ('until', models.IntegerField()),
                ('amountsince', models.IntegerField()),
                ('amountuntil', models.IntegerField()),
                ('tasa', models.FloatField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TasasCooviahorro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('amountMin', models.IntegerField()),
                ('termMin', models.IntegerField()),
                ('tasa', models.FloatField(max_length=20)),
            ],
        ),
    ]
