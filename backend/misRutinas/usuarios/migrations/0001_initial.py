# Generated by Django 4.2.1 on 2023-06-09 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentacion',
            fields=[
                ('id_alim', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=600)),
                ('summary', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'tips de alimentacion',
                'verbose_name_plural': 'Alimentaciones',
                'db_table': 'Alimentacion',
            },
        ),
    ]
