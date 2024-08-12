# Generated by Django 5.1 on 2024-08-12 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0005_delete_drinks_delete_drinktype'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeatRoast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meat_roast_level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_b', models.CharField(max_length=50)),
                ('price_b', models.PositiveIntegerField()),
                ('score_b', models.FloatField()),
                ('details_b', models.TextField(max_length=500)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pizzas.meatroast', verbose_name='Meat_Roast_Level')),
            ],
        ),
    ]
