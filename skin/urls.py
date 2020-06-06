from django.urls import path
from . import views


app_name = 'skin'  # here for namespacing of urls.

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.index, name="index"),
    path("check", views.check, name="check"),
    path("Img", views.Img, name="Img"),
    path("dis", views.dis, name="dis"),
    path("home", views.home, name="home"),
    path("patientreg", views.patientreg, name="patientreg"),
    path("patlogin", views.patlogin, name="patlogin"),
   
    path("disea", views.disea, name="disea"),
]