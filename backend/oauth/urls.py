from django.urls import path
from .views import *

urlpatterns = [
    path("signin/", sign_view, name="signnin")
]