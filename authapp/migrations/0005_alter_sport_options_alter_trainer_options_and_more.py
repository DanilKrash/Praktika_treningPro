# Generated by Django 4.2.11 on 2024-04-04 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('custom_authapp', '0004_remove_trainer_salary_trainer_experience_trainer_img_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sport',
            options={'verbose_name': 'Вид спорта', 'verbose_name_plural': 'Виды спорта'},
        ),
        migrations.AlterModelOptions(
            name='trainer',
            options={'verbose_name': 'Тренер', 'verbose_name_plural': 'Тренера'},
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='Login',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='Logout',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='SelectWorkout',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='Selectdate',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='TrainedBy',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата заявки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='phone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='sport',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='custom_authapp.sport', verbose_name='Вид спорта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('notviewed', 'Не одобрена'), ('yes', 'Одобрена'), ('no', 'Не одобрена')], default='notviewed', max_length=15, verbose_name='Статус заявки'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='trainer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='custom_authapp.trainer', verbose_name='Тренер'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='login',
            field=models.CharField(default=1, max_length=200, verbose_name='Начало'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='logout',
            field=models.CharField(default=1, max_length=200, verbose_name='Конец'),
            preserve_default=False,
        ),
    ]