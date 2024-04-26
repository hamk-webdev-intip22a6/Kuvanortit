from django.urls import path
from . import views

app_name = "gallerino"
urlpatterns = [
    path("", views.index, name="index")
]