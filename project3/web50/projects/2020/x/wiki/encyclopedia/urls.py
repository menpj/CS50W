from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("content",views.content,name="content"),
    path("wiki",views.wiki,name="wiki"),
    path("wiki/<str:name>",views.wiki,name="wiki")
]
