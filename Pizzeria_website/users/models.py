from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photo/", blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
    own_restaurants = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def post_save_user(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
