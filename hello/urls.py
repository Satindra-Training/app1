from django.urls import path

from . import views
#if we type http://localhost:3000/hello
#Child Routing
urlpatterns = [
    path("",views.hello),
    path("hii",views.hii)
    
]
