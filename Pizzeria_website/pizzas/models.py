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


