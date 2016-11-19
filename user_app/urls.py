from django.conf.urls import url
from views import userData, createUser

urlpatterns = [
    url(r'^', userData, name = "userData"),
    url(r'^add/', createUser, name = "createUser")
]

