# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from api.views import MyTokenObtainPairView, RegisterView, getRoutes, EditProfileView, CreateUserView

urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("", getRoutes),
    path("edit/user/<int:pk>", EditProfileView.as_view(), name="edit_user"),
    path("create/user", CreateUserView.as_view(), name="create_user"),
]
