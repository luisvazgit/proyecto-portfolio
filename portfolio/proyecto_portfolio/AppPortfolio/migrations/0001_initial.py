# Generated by Django 4.1 on 2022-12-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('institucion', models.CharField(max_length=50)),
                ('fecha', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Habilidades_blandas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Habildad', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Mis_datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
