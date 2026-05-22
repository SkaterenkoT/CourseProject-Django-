from rest_framework.viewsets import ModelViewSet
from .models import Archive
from .serializers import ArchiveSerializer


class ArchiveViewSet(ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
