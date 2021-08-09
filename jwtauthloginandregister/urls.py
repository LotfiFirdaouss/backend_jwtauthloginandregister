from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('account/',include('account.urls')),
]
