from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
	USER_TYPE_CHOICES = (
		(1, 'treasurer'),
		(2, 'secretary'),
		(3, 'supervisor'),
		(4, 'admin'),
	)

	user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)