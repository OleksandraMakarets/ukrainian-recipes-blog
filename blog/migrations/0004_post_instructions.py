# Generated by Django 4.2.14 on 2024-07-31 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_cooking_time_post_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='instructions',
            field=models.TextField(blank=True),
        ),
    ]
