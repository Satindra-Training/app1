from django.urls import path
from . import views
#Child Routes has been configured.
urlpatterns = [
    path("",views.home,name='home_page'),
    path("show",views.send,name='show')
    
]
