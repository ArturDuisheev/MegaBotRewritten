from django.urls import path

from .views import *

urlpatterns = [
    path('create_user/', get_user, name='create_user'),
    path('block_user/', block_user, name='block_user')
]
