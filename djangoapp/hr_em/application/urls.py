from django.urls import path

import application.views as v

urlpatterns = [
     path("", v.index, name="index"),
     path("register", v.RegisterView.as_view()),
     path("login", v.LoginView.as_view()),
     path("logout", v.logout_custom, name="logout"),
     path("list", v.ListView.as_view())
]