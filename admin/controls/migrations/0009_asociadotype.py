# Generated by Django 4.2.5 on 2024-07-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0008_sociales'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsociadoType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]