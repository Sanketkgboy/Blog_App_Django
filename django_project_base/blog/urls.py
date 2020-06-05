from django.urls import path
from . views import (
    PostListView,
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views


urlpatterns = [
	# path('home/', views.home, name='blog-home'),
	path('home/', PostListView.as_view(), name='blog-home'), # .as_view() will pass it as a view here
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # pk to grab a particular object
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('about/', views.about, name='blog-about'),
]