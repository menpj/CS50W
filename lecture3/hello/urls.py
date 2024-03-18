from . import views
from django.urls import path

urlpatterns = [
    path("", views.index,name="index"),
    path("noah",views.noah,name="noah") ,
    path("david",views.david,name="david")
]