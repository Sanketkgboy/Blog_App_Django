# when a user object saved post_save signal is triggered, in our case when user is created its triggered
from django.db.models.signals import post_save
# User model is what we call as a sender, it is what will be sending the signal
from django.contrib.auth.models import User
# receiver will be geting the signal and will perform some task
from django.dispatch import receiver
from . models import Profile


""" Receiver acepts two arguments post_save signal and the sender, i.e User. 
If the user is created then create the profile object with user=instance of user 
will be created"""
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

# Saves the profile object
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

""" To make the signals work, I am supposed to go to the users/apps.py and
inside the ready function I will have to import the signals. That is how django 
suggests to do it """
