# Generated by Django 4.0.5 on 2022-08-05 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('contenido', models.TextField(max_length=400)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='entrada')),
                ('autor', models.CharField(max_length=50)),
            ],
        ),
    ]
