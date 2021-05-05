from django.contrib.auth.models import User, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django_countries.fields import CountryField


class UserManager(BaseUserManager):
    """Create and manage users."""
    def create_user(self, first_name, last_name, email,
                    username=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not username:
            username = email.split('@')[0]

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password,
        username=None):
        user = self.create_user(
            first_name,
            last_name,
            email,
            username,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateTimeField(blank=True, null=True)
    bio = models.CharField(max_length=140, blank=True, null=True)
    #avatar = fields.ImageField(upload_to='avatar_photos/', blank=True, null=True)
    location = models.CharField(max_length=40, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    fav_animal = models.CharField(max_length=40, blank=True, null=True)
    hobby = models.CharField(max_length=40, blank=True, null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
