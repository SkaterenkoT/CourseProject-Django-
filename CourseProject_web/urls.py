from django.contrib import admin
from django.urls import path, include

from .views import supervisor_project, upload_document

from rest_framework.routers import DefaultRouter

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from users.views import UserViewSet
from topics.views import TopicViewSet
from projects.views import ProjectViewSet
from stages.views import StageViewSet
from documents.views import DocumentViewSet
from defenses.views import DefenseViewSet
from archives.views import ArchiveViewSet
from .views import (
    index,
    student_dashboard,
    supervisor_dashboard,
)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib.auth import views as auth_views

from .views import (
    index,
    student_dashboard,
    supervisor_dashboard,
    documents_page,
    stages_page,
)

from django.conf import settings
from django.conf.urls.static import static

from .views import documents_list

from .views import supervisor_dashboard

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'stages', StageViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'defenses', DefenseViewSet)
router.register(r'archives', ArchiveViewSet)

urlpatterns = [
    path('', index),

    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view()),

    path('api/token/refresh/', TokenRefreshView.as_view()),

    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema',
    ),

    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),

    path(
        'student/dashboard/',
        student_dashboard,
    ),

    path(
        'supervisor/dashboard/',
        supervisor_dashboard,
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        'student/documents/',
        documents_page,
        name='documents'
    ),

    path(
        'student/stages/',
        stages_page,
        name='stages'
    ),

    path(
        'student/upload/',
        upload_document,
        name='upload_document'
    ),

    path('documents/', documents_list, name='documents'),

    path('supervisor/project/<int:project_id>/', supervisor_project, name='supervisor_project'),

    path('supervisor/', supervisor_dashboard, name='supervisor_dashboard'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)