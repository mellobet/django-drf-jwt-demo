from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt import views as jwt_views
from demo_jwt_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # Demo test view
    path('demo/', views.DemoView.as_view(), name='demo'),
]
