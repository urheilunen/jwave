from django.urls import path
from .views import register, user_login, index

urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]