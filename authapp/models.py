from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    body = models.TextField(verbose_name='Описание')
    date = models.DateField(auto_now_add=True, verbose_name='Время')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Sport(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    img = models.ImageField(upload_to='sports/%Y/%m/%d/', verbose_name='Картинка')
    body = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'


class Trainer(models.Model):
    name = models.CharField(max_length=55, verbose_name='Имя')
    surname = models.CharField(max_length=55, verbose_name='Фамилия')
    img = models.ImageField(upload_to='trainers/%Y/%m/%d/', verbose_name='Фото')
    phone = models.CharField(max_length=25, verbose_name='Телефон')
    specialization = models.ForeignKey(Sport, on_delete=models.CASCADE, verbose_name='Специализация')
    experience = models.CharField(max_length=50, verbose_name='Опыт')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата устройства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'


class Attendance(models.Model):
    class Status(models.TextChoices):
        notviewed = 'notviewed', 'Не просмотрена'
        yes = 'yes', 'Одобрена'
        no = 'no', 'Не одобрена'

    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Почта')
    login = models.DateTimeField(max_length=200, verbose_name='Начало')
    logout = models.DateTimeField(max_length=200, verbose_name='Конец')
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, verbose_name='Вид спорта')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='Тренер')
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.notviewed,
                              verbose_name='Статус заявки')

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    physical = models.CharField(max_length=50, verbose_name='Уровень физической подготовки')
    preferences = models.ManyToManyField(Sport, blank=True, verbose_name='Предпочтения')
    img = models.ImageField(upload_to='users/%Y/%m/%d', verbose_name='Фото')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class CommentAttendence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, verbose_name='Тренировка')
    body = models.TextField(blank=False, verbose_name='Сообщение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Комментарий для тренировки'
        verbose_name_plural = 'Комментарии для тренировок'


class CommentTrainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='Тренер')
    body = models.TextField(blank=False, verbose_name='Сообщение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Комментарий для тренера'
        verbose_name_plural = 'Комментарии для тренеров'
