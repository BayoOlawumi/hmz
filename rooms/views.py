from django.shortcuts import render
from .serializers import RoomSerializer, RoomCategorySerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions
from .models import Room, RoomCategory





class RoomViewSet(viewsets.ReadOnlyModelViewSet):
   
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomCategoryViewset(viewsets.ModelViewSet):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer



