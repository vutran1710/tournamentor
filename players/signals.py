import re
import exrex
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import (
    Profile,
    SECRET_REGEX,
    PASSWORD_REG,
)


def email_to_username(email):
    return re.sub("@", "__", email)


@receiver(pre_save, sender=User)
def create_user_with_email(sender, instance, **kwargs):
    if instance.id:
        return

    instance.password = exrex.getone(PASSWORD_REG)
    instance.username = email_to_username(instance.email)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        for _ in range(5):
            try:
                Profile.objects.create(user=instance, secret=exrex.getone(SECRET_REGEX))
            except Exception as err:
                print("error %s" % err)
                print("Retry creating profile")
