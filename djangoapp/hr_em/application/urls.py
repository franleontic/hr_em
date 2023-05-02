from django.urls import path
from django.conf.urls import url

import application.views as v

urlpatterns = [
     path("", v.index, name="index"),
]