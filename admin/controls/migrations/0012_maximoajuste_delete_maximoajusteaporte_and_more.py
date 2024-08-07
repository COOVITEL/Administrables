# Generated by Django 4.2.5 on 2024-07-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0011_alter_ajustesaportes_aportemax_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaximoAjuste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='MaximoAjusteAporte',
        ),
        migrations.DeleteModel(
            name='MaximoAjusteCDAT',
        ),
        migrations.DeleteModel(
            name='MaximoAjusteCooviahorro',
        ),
        migrations.DeleteModel(
            name='MaximoAjustePlazo',
        ),
        migrations.DeleteModel(
            name='MaximoAjusteScore',
        ),
    ]
