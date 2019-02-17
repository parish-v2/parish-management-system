from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
	TREASURER = 1
	SECRETARY = 2
	SUPERVISOR = 3
	ADMIN = 4
	USER_TYPE_CHOICES = (
		(TREASURER, 'treasurer'),
		(SECRETARY, 'secretary'),
		(SUPERVISOR, 'supervisor'),
		(ADMIN, 'admin'),
	)

	user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)