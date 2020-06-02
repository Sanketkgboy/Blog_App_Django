from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# UserRegisterForm class is written for adding email field in the UserCreation Form 
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	# class Meta provides the nested name space for configs and keeps them in one place
	class Meta:
		model = User # Model that I will be dealing with
		# Fields that I want and in what order
		fields = ['username', 'email', 'password1', 'password2']