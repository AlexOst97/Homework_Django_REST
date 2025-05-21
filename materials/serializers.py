from rest_framework import serializers
from .models import Сourse, Lesson


class СourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Сourse
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
