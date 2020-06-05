from django.shortcuts import render, redirect
"""UserCreationForm that already exists in django, these forms are classes 
 that will get converted into html"""
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
"""Instead of UserCreationForm using UserRegisterForm by adding email field in 
UserCreationForm. Also importing UserUpdateForm, ProfileUpdateForm for updating
User fields and Image of profile"""
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
	if request.method == 'POST':
		# Create a form instance and populate it with the data from the request 
		form = UserRegisterForm(request.POST) #binded the data with the form
		if form.is_valid():
			form.save() # saves the form and we can see the user in the admin portal 
			# We can find all the validated data in the form.cleaned_data dictionary
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You can log in now')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, 
								   request.FILES, 
								   instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {'u_form': u_form, 'p_form': p_form}
	return render(request, 'users/profile.html', context)

