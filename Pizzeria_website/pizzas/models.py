from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    score = models.FloatField()
    details = models.TextField(max_length=300)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"Pizza {self.name}"
