from django.urls import path
from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PaymentListAPIView, PaymentRetrieveAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, PaymentDestroyAPIView


app_name = UsersConfig.name
router = DefaultRouter()
router.register('', UserViewSet)
urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_retrieve'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/<int:pk>/update/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    path('payment/<int:pk>/destroy/', PaymentDestroyAPIView.as_view(), name='payment_destroy'),
]
urlpatterns += router.urls