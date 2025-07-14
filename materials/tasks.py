from datetime import timedelta, timezone

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription, Сourse
from users.models import User


@shared_task
def updating_courses(course_id):
    """Рассылка писем пользователям об обновлении материалов курса"""

    course = Сourse.objects.filter(pk=course_id).first()
    users = User.objects.all()
    for user in users:
        subscription = Subscription.objects.filter(user=user, course=course).first()
        if subscription:
            send_mail(
                subject="Обновление курса!",
                message=f'Здравствуйте! Ваш Курс "{course.name}" успешно обновлен!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )

    @shared_task
    def block_last_login():
        users = User.objects.filter(last_login__isnull=False)
        for user in users:
            if timezone.now() - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()
                print(f"Пользователь {user.email} заблокирован")
            else:
                print(f"Пользователь {user.email} активен")
