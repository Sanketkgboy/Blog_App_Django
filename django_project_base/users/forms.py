from django import forms 
from django.contrib.auth.models import User
# Had to add email field in UserCreationForm so imported that.
from django.contrib.auth.forms import UserCreationForm
# Imported profile model to update the profile image.
from . models import Profile


# UserRegisterForm class is written for adding email field in the UserCreation Form 
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	# class Meta provides the nested name space for configs and keeps them in one place
	class Meta:
		model = User # Model that I will be dealing with
		# Fields that I want and in what order
		fields = ['username', 'email', 'password1', 'password2']


"""Model Forms allow us to create a form that allows us to work with a specific 
database model, here I want a form that will update my user model"""
class  UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		# Fields that I want to update
		fields = ['username', 'email'] 

"""I want to update image/profile pic as well but image is in other Profile model
I need to import the Profile model at the top"""
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

"""Now UserUpdateForm and ProfileUpdateForm will be imported in 'users/views.py' for 
further process"""


