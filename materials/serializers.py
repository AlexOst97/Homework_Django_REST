from rest_framework import serializers
from .models import Сourse, Lesson

class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class СourseSerializers(serializers.ModelSerializer):

    lesson = LessonSerializers(many=True)
    amount_lesson = serializers.SerializerMethodField()

    def get_amount_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Сourse
        fields = ("name", "description", "preview", "lesson", "amount_lesson")