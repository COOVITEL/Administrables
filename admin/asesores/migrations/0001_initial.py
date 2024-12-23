# Generated by Django 4.2.5 on 2024-12-17 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Asesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('document', models.IntegerField()),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asesores.sucursal')),
            ],
        ),
    ]