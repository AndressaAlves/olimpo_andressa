from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.feed, name='feed'),
    url(r'^ask/',views.ask,name='ask'),
]
