from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    score = models.PositiveIntegerField()
    details = models.TextField(max_length=300)

    def __str__(self):
        return f"Pizza {self.name}"
