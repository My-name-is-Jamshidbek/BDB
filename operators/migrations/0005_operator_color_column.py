# Generated by Django 5.0.1 on 2024-01-13 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0004_operator_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='color_column',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
