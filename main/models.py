# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Categories(models.Model):
    category = models.CharField('Категории', max_length=100)
    slug = models.SlugField(verbose_name='Транслит', null=True)


    class Meta():
        db_table = 'categories'
        ordering = ['category']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, default=User)
    title = models.CharField(verbose_name='Заголовок поста', max_length=100)
    image = models.ImageField(null=True, blank=True)
    post = models.TextField(verbose_name='Текст поста', blank=True)
    categories = models.ForeignKey(Categories, blank=True, verbose_name='Категория', on_delete=models.CASCADE)
    created_date = models.DateTimeField('Дата создания',
        default=timezone.now)


    class Meta():
        db_table = 'Post'
        ordering = ['title']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:index')
