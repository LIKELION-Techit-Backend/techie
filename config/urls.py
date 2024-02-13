"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import LoginAPI, MemberListAPI, PendingAPI, TeamListAPI, LectureListAPI, LectureAPI, CourseAPI, CourseListAPI, MemberAPI, TeamAPI, TakenAPI, TakenListAPI, SyncAPI, InitializeDataAPI
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Techit Together",
        default_version='1.0.0',
        description="해당 문서 설명(예: humanscape-project API 문서)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=""),  # 부가정보
        license=openapi.License(name="sjsu-likelion"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/member/', MemberListAPI.as_view()),
    path('api/member/<int:id>', MemberAPI.as_view()),
    path('api/login', LoginAPI.as_view()),
    path('api/team/', TeamListAPI.as_view()),
    path('api/team/<int:id>', TeamAPI.as_view()),
    path('api/lecture/', LectureListAPI.as_view()),
    path('api/lecture/<int:id>', LectureAPI.as_view()),
    path('api/course/', CourseListAPI.as_view()),
    path('api/course/<int:id>', CourseAPI.as_view()),
    path('api/taken', TakenListAPI.as_view()),
    path('api/taken/<int:id>', TakenAPI.as_view()),
    path('api/pending', PendingAPI.as_view()),
    path('api/sync', SyncAPI.as_view()),
    # path('api/initialize', InitializeDataAPI.as_view()),
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc-v1'),
]
