from rest_framework.routers import DefaultRouter
from . import views

#The various routers

room_router = DefaultRouter()

room_router.register(r'room-list', views.RoomViewSet)
room_router.register(r'room-category', views.RoomCategoryViewset)