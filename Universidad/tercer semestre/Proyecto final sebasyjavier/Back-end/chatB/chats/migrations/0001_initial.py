# Generated by Django 4.1.3 on 2023-06-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remitente', models.CharField(max_length=100)),
                ('destinatario', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('fechaEnvio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]