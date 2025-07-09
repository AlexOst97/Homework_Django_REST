from django.db.models.expressions import result
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Сourse
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@yandex.ru")
        self.course = Сourse.objects.create(
            name="Курс 1", description="Что-то про курс", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            course=self.course,
            name="Урок 1",
            description="Что-то про урок",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve(self):
        url = reverse("materials:lesson-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("description"), self.lesson.description)

    def test_create(self):
        url = reverse("materials:lesson-create")
        data = {"name": "Урок 2"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_update(self):
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {"description": "Урок 2"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("description"), "Урок 2")

    def test_delete(self):
        url = reverse("materials:lesson-destroy", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_list(self):
        url = reverse("materials:lesson-list")
        response = self.client.get(url)
        data = response.json()
        r1 = data["results"]
        r2 = [
            {
                "id": 4,
                "name": "Урок 1",
                "description": "Что-то про урок",
                "preview": None,
                "video_link": None,
                "course": self.course.pk,
                "owner": self.user.pk,
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(r1, r2)
