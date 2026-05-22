from rest_framework.viewsets import ModelViewSet
from .models import Stage
from .serializers import StageSerializer


class StageViewSet(ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
