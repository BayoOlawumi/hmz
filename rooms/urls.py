from django.urls import path, include
from . import views
from . import routers

app_name = 'Rooms'


urlpatterns = [
   
    path('', include(routers.room_router.urls)),
]