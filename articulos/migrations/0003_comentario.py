# Generated by Django 4.1.6 on 2023-02-02 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_alter_entrada_contenido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('comentario', models.TextField(max_length=400)),
            ],
        ),
    ]