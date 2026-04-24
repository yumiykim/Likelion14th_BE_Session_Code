from django.urls import path

from . import views
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup"),
]