from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView
from .views import *


urlpatterns = [
    path('movie-list/', MovieAPIList.as_view(), name="movie-list"),
    path('movie/<slug:slug>/', MovieAPIGet.as_view(), name="movie-detail"),
    path('profile/', FavMovies.as_view(), name="profile"),
    path('drf-auth/', include('rest_framework.urls')),
    path('v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
