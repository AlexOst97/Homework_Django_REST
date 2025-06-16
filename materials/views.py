from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from materials.models import Сourse, Lesson, Subscription
from materials.pagination import MyPageNumberPagination
from materials.serializers import (
    СourseSerializers,
    LessonSerializers,
    SubscriptionSerializers,
)
from users.permissions import IsModerators, IsOwners
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from materials.tasks import updating_courses


# Сourse
class СourseViewSet(viewsets.ModelViewSet):
    serializer_class = СourseSerializers
    queryset = Сourse.objects.all()
    pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == ["create"]:
            self.permission_classes = [~IsModerators]
        elif self.action == ["update", "retrieve"]:
            self.permission_classes = [IsModerators | IsOwners]
        elif self.action == ["destroy"]:
            self.permission_classes = [~IsOwners | IsOwners]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        updating_courses.delay(instance.pk)
        return instance


# Lesson
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerators]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerators | IsOwners]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerators | IsOwners]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPageNumberPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerators | IsOwners]


# Subscription
class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerators]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Сourse, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"

        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "подписка добавлена"

        return Response({"message": message})
