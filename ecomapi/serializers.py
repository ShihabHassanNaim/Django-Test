from rest_framework import serializers
from .models import Sp

class Spserializers(serializers.ModelSerializer):
    class Meta:
        model = Sp
        fields = '__all__'
    
    