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
    roast_choice = [
        ("medium", "Medium"),
        ("medium_rare", "Medium Rare"),
        ("rare", "Rare"),
        ("well_done", "Well Done"),
    ]
    meat_roast_level = models.CharField(max_length=50, choices=roast_choice)

    def __str__(self):
        return self.meat_roast_level


class Burger(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    score = models.FloatField()
    details = models.TextField(max_length=500)
    category = models.ForeignKey(MeatRoast, null=True,
                                 on_delete=models.PROTECT, verbose_name="Meat_Roast_Level")
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Restaurants(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True)
    burgers = models.ManyToManyField(Burger, related_name="restaurant", null=True, blank=True)
    pizzas = models.ManyToManyField(Pizza, related_name="restaurant", null=True, blank=True)

    def __str__(self):
        return self.name
