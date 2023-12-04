from .BagSerilizer import BagSerilizer
from .models import Bag
from rest_framework import viewsets

class BagViewSet(viewsets.ModelViewSet):
    queryset=Bag.objects.all()
    serializer_class=BagSerilizer