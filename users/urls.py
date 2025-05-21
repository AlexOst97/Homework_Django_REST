from django.urls import path
from users.apps import UsersConfig
from .views import UserListAPIView, UserRetrieveAPIView, UserCreateAPIView, UserUpdateAPIView, UserDestroyAPIView


app_name = UsersConfig.name
urlpatterns = [
    path('', UserListAPIView.as_view(), name='users_list'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='users_retrieve'),
    path('users/create/', UserCreateAPIView.as_view(), name='users_create'),
    path('users/<int:pk>/update/', UserUpdateAPIView.as_view(), name='users_update'),
    path('users/<int:pk>/destroy/', UserDestroyAPIView.as_view(), name='users_destroy'),
]
