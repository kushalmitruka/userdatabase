from django.conf.urls import url
from views import userData, createUser

urlpatterns = [
    url(r'^', userData, name = "userData"),
    url(r'^POST/', createUser, name = "createUser")
]

