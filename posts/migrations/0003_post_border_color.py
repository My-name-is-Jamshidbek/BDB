# Generated by Django 5.0.1 on 2024-01-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='border_color',
            field=models.TextField(null=True),
        ),
    ]
