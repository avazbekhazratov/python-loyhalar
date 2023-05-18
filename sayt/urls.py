from django.urls import path

from .views import *
from .auth import sing_in, sing_up, sing_out

urlpatterns = [
    path("", index, name="home"),
    path("contact/", cnt, name="contact"),
    path("ctg/<int:_id>/", ctg, name="ctg"),
    path("view/<int:pk>/", view, name="view"),
    path("search/", srch, name="search"),

    path("login/", sing_in, name="login"),
    path("regis/", sing_up, name="regis"),
    path("logout/", sing_out, name="logout"),
    path("logout/<int:conf>/", sing_out, name="logout-conf")


]
