# Generated by Django 5.0.1 on 2024-01-03 09:35

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
