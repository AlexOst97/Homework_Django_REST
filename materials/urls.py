from django.urls import path
from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter
from .views import СourseViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonDestroyAPIView


router = DefaultRouter()
router.register(r"courses", СourseViewSet, basename="courses")

app_name = MaterialsConfig.name
urlpatterns = [
    path('', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='update'),
    path('lesson/<int:pk>/destroy/', LessonDestroyAPIView.as_view(), name='destroy'),
]

urlpatterns += router.urls
