# Generated by Django 3.1.2 on 2020-10-15 04:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('titulo', models.CharField(max_length=100)),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID pal juego gei', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(help_text='Descripción del juego', max_length=1000)),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.ManyToManyField(to='dotgames.Genero')),
            ],
        ),
    ]
