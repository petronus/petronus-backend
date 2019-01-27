from django.db import models

# Create your models here.
from Users.models import User


class Pet(models.Model):
	elected_term = models.ForeignKey(
		User, 
		on_delete=models.CASCADE,
	)
	petID = models.CharField(max_length=255)
	petName = models.CharField(max_length=255)
	attribs = models.CharField(max_length=255)