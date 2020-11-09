from django.urls import path
from django.conf.urls import url

from sample import views as SampleViews


urlpatterns = [
    path('', SampleViews.index, name='index'),
]