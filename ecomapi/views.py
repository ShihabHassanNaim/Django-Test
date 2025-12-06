from .models import Sp
from .serializers import Spserializers
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated




class SpModel(viewsets.ModelViewSet):
    queryset = Sp.objects.all()
    serializer_class = Spserializers
    