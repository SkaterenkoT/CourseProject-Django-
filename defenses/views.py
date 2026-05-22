from rest_framework.viewsets import ModelViewSet
from .models import Defense
from .serializers import DefenseSerializer


class DefenseViewSet(ModelViewSet):
    queryset = Defense.objects.all()
    serializer_class = DefenseSerializer
