from django.contrib import admin

# These are views that django provides us for login and logout  
from django.contrib.auth import views as auth_views

# If MEDIA_URL is defined as /media/, to serve the uploaded file we need to import settings, static
from django.conf import settings
from django.conf.urls.static import static
# imported include to include urls in blog app
from django.urls import path, include
# Imported user view
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('blog/', include('blog.urls')),
] 

""" In url patterns defined above, the LoginView and LogoutView are the class based views, these builtin
    views help us to handle the forms logic stuff for us but it will not handle
    the templates """

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)













