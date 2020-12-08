
from django.urls import path
from . import views

app_name = 'video'
urlpatterns = [
    path('', views.gravarVideo, name='gravar-video'),
    path('gravar-video/', views.gravarVideo, name='gravar-video'),
]
