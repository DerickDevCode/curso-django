# Generated by Django 5.0 on 2023-12-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0004_populando_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]