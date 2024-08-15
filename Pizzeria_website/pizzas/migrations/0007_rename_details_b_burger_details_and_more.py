# Generated by Django 5.1 on 2024-08-15 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0006_meatroast_burger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='burger',
            old_name='details_b',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='burger',
            old_name='name_b',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='burger',
            old_name='price_b',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='burger',
            old_name='score_b',
            new_name='score',
        ),
        migrations.AddField(
            model_name='burger',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
