# Generated by Django 4.2.14 on 2024-07-31 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cooking_time',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='ingredients',
            field=models.TextField(blank=True),
        ),
    ]
