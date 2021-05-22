from django.urls import path
from .views import user_logout, signup, user_login

app_name = 'account'

urlpatterns = [
    path('logout/', user_logout, name='user_logout'),
    path('signup/', signup, name='user_register'),
    path('login/', user_login, name='user_login'),
]
