from django.db import models
# Importing User model to create a profile model with one t onw relationship with the user model
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE) # If user deleted, delete profile
	# pip install Pillow for woring with images
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	# Printing out profile in a readable way.
	def __str__(self):
		return f'{self.user.username} Profile'