from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=256)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=25)
    phone = models.CharField(max_length=15, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_custom(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)
