from django.contrib.auth import views as auth_views
from .views import RegisterView, CustomLoginView, CustomLogoutView,ProfileView
from django.urls import path
app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    ]