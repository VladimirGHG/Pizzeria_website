# Generated by Django 5.1 on 2024-08-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0010_restaurants_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
