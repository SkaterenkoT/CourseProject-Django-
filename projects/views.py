from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Project.objects.all()

        if user.role == 'supervisor':
            return Project.objects.filter(supervisor=user)

        if user.role == 'student':
            return Project.objects.filter(student=user)

        return Project.objects.none()