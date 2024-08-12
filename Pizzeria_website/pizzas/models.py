from django.db import models


class DoughType(models.Model):
    dough = models.CharField(max_length=20, db_index=True, verbose_name="Dough type")

    def __str__(self):
        return self.dough


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    score = models.FloatField()
    details = models.TextField(max_length=300)
    image = models.ImageField(null=True, blank=True)

    category = models.ForeignKey('DoughType', null=True,
                                 on_delete=models.PROTECT, verbose_name="Dough")

    def __str__(self):
        return f"Pizza {self.name}"


class MeatRoast(models.Model):
    meat_roast_level = models.CharField(max_length=50)

    def __str__(self):
        return self.meat_roast_level


class Burger(models.Model):
    name_b = models.CharField(max_length=50)
    price_b = models.PositiveIntegerField()
    score_b = models.FloatField()
    details_b = models.TextField(max_length=500)
    category_b = models.ForeignKey('MeatRoast', null=True,
                                   on_delete=models.PROTECT, verbose_name="Meat_Roast_Level")

    def __str__(self):
        return self.name_b
