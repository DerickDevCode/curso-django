# Generated by Django 5.0 on 2023-12-26 18:53

from django.db import migrations
from django.utils.text import slugify


def popular_slug(apps, schema_editor):
    Modulo = apps.get_model('modulos', 'Modulo')
    for modulo in Modulo.objects.all():
        modulo.slug = slugify(modulo.titulo)
        modulo.save()


class Migration(migrations.Migration):
    dependencies = [
        ('modulos', '0003_modulo_slug'),
    ]

    operations = [
        migrations.RunPython(popular_slug)
    ]
