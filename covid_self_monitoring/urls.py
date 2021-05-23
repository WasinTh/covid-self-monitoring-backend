from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Covid Self Monitoring API",
        default_version='v1',
        description="bla bla..",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api-token-auth/', jwt_views.TokenObtainPairView.as_view()),
    path('api-token-refresh/', jwt_views.TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('monitor/', include('monitor.urls')),
]
