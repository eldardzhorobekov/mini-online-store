from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('signin', views.SignInView.as_view(), name='signin'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.ProfileEditView.as_view(), name='profile-edit')
]
