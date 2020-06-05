from django.db import models
# Importing User model to create a profile model with one t onw relationship with the user model
from django.contrib.auth.models import User
# To resize the image we need this library to interact with image
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE) # If user deleted, delete profile
	# pip install Pillow for woring with images
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	# Printing out profile in a readable way.
	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save() # run the save method of parent class

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300) # The target resolution
			img.thumbnail(output_size)
			img.save(self.image.path) # image will be saved at same path


"""Note: If you want to delete older images, i.e after overwriting.
then "pip install django-cleanup" (run without quotes). in settings.py
under INSTALLED_APPS add 'django_cleanup' and it will auto delete old files""" 