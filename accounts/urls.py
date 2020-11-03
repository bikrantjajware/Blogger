from django.urls import path
from  django.contrib.auth import views as auth_view
from . import  views

app_name = 'accounts'
urlpatterns = [
    path('signup/',views.signup.as_view(),name='signup'),
    path('login/',auth_view.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
]