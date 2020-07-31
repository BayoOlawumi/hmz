from rest_framework.serializers import(
    HyperlinkedIdentityField,
    ModelSerializer, 
    SlugRelatedField,
    HyperlinkedRelatedField,
)
from .models import Room,RoomCategory

class RoomSerializer(ModelSerializer):
    category = SlugRelatedField(slug_field='name', queryset=RoomCategory.objects.all())
    class Meta:
        model = Room
        fields = (
            'number',
            'condition',
            'status',
            'date_issued',
            'category',
        )



class RoomCategorySerializer(ModelSerializer):

    rooms = RoomSerializer(many=True)
    class Meta:
        model = RoomCategory
        fields = (
            'name',
            'unique_color',
            'max_room_no',
            'rooms',
        )