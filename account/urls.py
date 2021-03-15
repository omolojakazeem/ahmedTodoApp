from django.urls import path
from .views import user_logout

app_name = 'account'

urlpatterns = [
    path('/logout', user_logout, name='user_logout')
]
