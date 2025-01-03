# Generated by Django 4.2.5 on 2024-12-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrosSimulacionesCreditos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('document', models.IntegerField()),
                ('dateborn', models.DateTimeField()),
                ('dateafi', models.DateTimeField()),
                ('typeAsociado', models.CharField(max_length=100)),
                ('typeContract', models.CharField(max_length=100)),
                ('seniority', models.DateTimeField()),
                ('payForm', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('warranty', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('others', models.CharField(max_length=100)),
                ('cuotasDes', models.CharField(max_length=100)),
                ('cuotasCen', models.CharField(max_length=100)),
                ('cooviahorro', models.CharField(max_length=100)),
                ('cdat', models.CharField(max_length=100)),
                ('aportes', models.CharField(max_length=100)),
                ('linea', models.CharField(max_length=100)),
                ('credit', models.CharField(max_length=100)),
                ('cuotas', models.CharField(max_length=100)),
                ('monto', models.CharField(max_length=100)),
            ],
        ),
    ]
