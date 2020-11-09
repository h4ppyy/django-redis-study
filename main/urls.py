from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('', include('sample.urls'))
]
