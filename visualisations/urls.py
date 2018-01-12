from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'charts/line/', views.line_chart),
]