from . import views
from django.urls import path

urlpatterns = [
    path("", views.index,name="index"),
    path("greet",views.greet,name="greet"),
    path("<str:name>",views.greet,name="greet")
    
]