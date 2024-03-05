from django.urls import re_path as url
from . import views
app_name='catalog'

urlpatterns = [
    url(r"^$", views.index, name="index"),

]
