from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from materials.models import Сourse, Lesson
from materials.serializers import СourseSerializers, LessonSerializers
from users.permissions import IsModerators, IsOwners


class СourseViewSet(viewsets.ModelViewSet):
    serializer_class = СourseSerializers
    queryset = Сourse.objects.all()

    def get_permissions(self):
        if self.action == ['create']:
            self.permission_classes = [~IsModerators]
        elif self.action == ['update', 'retrieve']:
            self.permission_classes = [IsModerators | IsOwners]
        elif self.action == ['destroy']:
            self.permission_classes = [~IsOwners | IsOwners]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerators]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


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


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerators | IsOwners]
