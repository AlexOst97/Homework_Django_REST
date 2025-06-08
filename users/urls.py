from django.urls import path
from rest_framework.permissions import AllowAny
from users.apps import UsersConfig
from .views import (
    UserCreateAPIView,
    PaymentListAPIView,
    PaymentRetrieveAPIView,
    PaymentCreateAPIView,
    PaymentUpdateAPIView,
    PaymentDestroyAPIView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = UsersConfig.name

urlpatterns = [
    path("payments/",
         PaymentListAPIView.as_view(),
         name="payment-list"
         ),
    path(
        "payment/<int:pk>/",
        PaymentRetrieveAPIView.as_view(),
        name="payment-retrieve"
    ),
    path("payment/create/",
         PaymentCreateAPIView.as_view(),
         name="payment-create"
         ),
    path(
        "payment/<int:pk>/update/",
        PaymentUpdateAPIView.as_view(),
        name="payment-update",
    ),
    path(
        "payment/<int:pk>/destroy/",
        PaymentDestroyAPIView.as_view(),
        name="payment-destroy",
    ),
    path("register/",
         UserCreateAPIView.as_view(),
         name="register"
         ),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=[AllowAny,]),
        name="login",
    ),
    path(
        "refresh/",
        TokenRefreshView.as_view(permission_classes=[AllowAny,]),
        name="refresh",
    ),
]
