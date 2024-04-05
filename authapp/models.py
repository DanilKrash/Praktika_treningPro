from django.contrib.auth.models import User
from django.db import models


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
    phone = models.CharField(max_length=25)
    specialization = models.ForeignKey(Sport, on_delete=models.CASCADE, verbose_name='Специализация')
    experience = models.CharField(max_length=50, verbose_name='Опыт')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'


class Attendance(models.Model):
    class Status(models.TextChoices):
        notviewed = 'notviewed', 'Новая'
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

