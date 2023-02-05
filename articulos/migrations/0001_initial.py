# Generated by Django 4.1.6 on 2023-02-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=400)),
                ('imagen', models.URLField()),
                ('autor', models.CharField(max_length=50)),
            ],
        ),
    ]