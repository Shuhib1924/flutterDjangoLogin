from django.db import models

# Create your models here.
# In authentication/models.py
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add any additional fields here

    class Meta:
        app_label = "authentication"
        # Define unique related names for groups and user_permissions
        permissions = [("can_do_something", "Can perform some action")]
