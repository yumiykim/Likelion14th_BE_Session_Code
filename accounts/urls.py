from django.urls import path

from . import views
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('longin/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', sighup, name="signup"),
]