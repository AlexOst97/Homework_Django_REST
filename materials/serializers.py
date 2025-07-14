from rest_framework import serializers

from .models import Lesson, Subscription, Сourse
from .validators import YouTubeValidator


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YouTubeValidator(field="video_link")]


class SubscriptionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"


class СourseSerializers(serializers.ModelSerializer):

    lesson = LessonSerializers(many=True, read_only=True)
    amount_lesson = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()

    def get_amount_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        user = self.context["request"].user
        return (
            Subscription.objects.all().filter(user=user).filter(course=course).exists()
        )

    class Meta:
        model = Сourse
        fields = (
            "id",
            "name",
            "description",
            "preview",
            "lesson",
            "amount_lesson",
            "subscription",
        )
