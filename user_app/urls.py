from django.conf.urls import url
from views import userData

urlpatterns = [
    url(r'^', userData, name = "userData"),
]
