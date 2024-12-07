from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view,name='login_view'),
    path('register/',register_view,name='register_view'),
    path('list/',movies_view,name='movies_view'),
    path('logout/',logout_view,name='logout_view'),

]