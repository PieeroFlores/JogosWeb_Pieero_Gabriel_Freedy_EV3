# Generated by Django 3.1.2 on 2020-11-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotgames', '0006_juego_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='portada',
            field=models.ImageField(default='dotgames/static/img/no.png', upload_to='dotgames'),
        ),
    ]
