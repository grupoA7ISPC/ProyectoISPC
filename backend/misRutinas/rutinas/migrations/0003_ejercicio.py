# Generated by Django 4.2.1 on 2023-06-12 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rutinas', '0002_zonacuerpo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id_ejerc', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fk_zonacuerpo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rutinas.zonacuerpo')),
            ],
            options={
                'verbose_name': 'Ejercicio para una Zona',
                'verbose_name_plural': 'Ejercicios',
                'db_table': 'Ejercicio',
            },
        ),
    ]
