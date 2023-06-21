# Generated by Django 4.2.1 on 2023-06-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id_sub', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=370)),
                ('price', models.FloatField()),
                ('dur_dias', models.IntegerField()),
            ],
            options={
                'verbose_name': 'suscripciones',
                'verbose_name_plural': 'suscripciones',
                'db_table': 'Suscripcion',
            },
        ),
    ]
