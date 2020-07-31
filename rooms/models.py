from django.db import models
from django.utils import timezone

# Create your models here.

class RoomCategory(models.Model):

    """[This handles every category of room created]
    """

    name = models.CharField(max_length=30, blank=False, verbose_name="Class of room", unique=True)
    unique_color = models.CharField(max_length=35, unique=True, blank=True, help_text="This should an HEX code for every unique class of room")
    max_room_no= models.PositiveSmallIntegerField(blank=False)


    def __str__(self):
        return  self.name



class Room(models.Model):
    
    """This handles the Room Model

    Args:
        models ([Model]): [Every Room in a hotel]

    Returns:
        [str]: [The name, condition and status of the room]
    """
    BAD='bad'
    GOOD='good'
    CONDITION = (
        (BAD, 'Bad'),
        (GOOD,'Good'),
    )

    AVAILABLE= 'free'
    BOOKED= 'booked'
    OCCUPIED= 'occupied'
    STATUS = (
        (OCCUPIED,'Unavailable'),
        (BOOKED,'Booked'),
        (AVAILABLE,'Available'),
    )

    number = models.PositiveSmallIntegerField(unique=True, blank=False)
    condition= models.CharField(choices=CONDITION, default=GOOD, max_length=20)
    status= models.CharField(choices=STATUS, default=AVAILABLE, max_length=20)
    date_issued= models.DateTimeField(auto_now=True)
    category= models.ForeignKey(RoomCategory,on_delete=models.CASCADE, null=True, related_name='rooms')
   
    
    def __str__(self):
        return '{}: {} and {}'.format(str(self.number), self.condition, self.status)

