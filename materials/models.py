from django.db import models


class Сourse(models.Model):

    name = models.CharField(max_length=150, verbose_name='Название', help_text='Введите название курса')
    description = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Введите описание курса')
    preview = models.ImageField(upload_to='catalog/image', blank=True, null=True, verbose_name='Превью (картинка)', help_text='Загрузите картинку')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Lesson(models.Model):

    name = models.CharField(max_length=150, verbose_name='Название', help_text='Введите название урока')
    description = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Введите описание урока')
    preview = models.ImageField(upload_to='catalog/image', blank=True, null=True, verbose_name='Превью (картинка)', help_text='Загрузите картинку')
    video_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на видео', help_text='Вставьте ссылку на видео')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'