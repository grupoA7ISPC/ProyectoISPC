# Generated by Django 4.2.1 on 2023-06-03 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('periodo', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Pago suscripciones',
                'verbose_name_plural': 'Pagos',
                'db_table': 'Pago',
            },
        ),
    ]
