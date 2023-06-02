from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api import views



urlpatterns = [
    path("", views.home, name="api_home"),

    # masters
    path("masters", views.masters, name="api_masters_all"),

    # jwt urls
    path("token", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
