#  coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from mysite.mymodule import RandomFileName


class StatusOfTasks(models.Model):
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Profile(models.Model):
    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'


    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    user_type = models.IntegerField()
    phone = models.CharField(max_length = 20,blank = True)
    email = models.CharField(max_length = 40,blank = True)
    status = models.ForeignKey(StatusOfTasks,blank = True, null=True)
    start = models.DateTimeField(null= True, blank = True)
    finish = models.DateTimeField(null= True, blank = True)





class Tasks(models.Model):
    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Задания'
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    finish = models.DateTimeField(null= True, blank = True)
    status = models.ForeignKey(StatusOfTasks)
    description = models.CharField(max_length=700)
    comments = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Files(models.Model):
    class Meta:
        verbose_name = 'Прикрепленные файлы'
        verbose_name_plural = 'Прикрепленные файлы'

    data =  models.ImageField(upload_to=RandomFileName('images'))
    task = models.ForeignKey(Tasks)




