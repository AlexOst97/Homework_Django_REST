from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Сourse, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Номер телефона"
    )
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Город")
    avatar = models.ImageField(
        upload_to="users/image", blank=True, null=True, verbose_name="Изображение"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"


class Payment(models.Model):

    cash = "Наличные"
    translation = "Перевод"

    CHOICES = [
        (cash, "Наличные"),
        (translation, "Перевод"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_payment",
        verbose_name="Пользователь",
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    course = models.ForeignKey(
        Сourse,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="paid_course",
        verbose_name="Оплаченный курс",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="paid_lesson",
        verbose_name="Оплаченный урок",
    )
    payment_amount = models.IntegerField(
        null=True, blank=True, verbose_name="Сумма оплаты"
    )
    paid_course_or_lesson = models.CharField(
        max_length=10, choices=CHOICES, default="cash", verbose_name="Способ оплаты"
    )
    session_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Id сессия",
    )
    link = models.URLField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Ссылка на оплату",
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.id} {self.user} - {self.payment_amount}"
