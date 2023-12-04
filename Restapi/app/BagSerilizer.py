from rest_framework import serializers
from .models import Bag

class BagSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Bag
        fields='__all__'