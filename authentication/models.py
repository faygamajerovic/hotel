from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    VISITOR = 1
    STAFF = 2

    ROLE_CHOICES = (
        (VISITOR, 'visitor'),
        (STAFF, 'staff'),
    )

    user_type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=VISITOR)


