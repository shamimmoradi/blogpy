from django.urls import path , include 
from django.conf.urls import url , include
from blog import views
urlpatterns = [
    path("",views.IndexPage.as_view())
]
