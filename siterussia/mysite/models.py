from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos", verbose_name='Фото1', blank=True)
    photo1 = models.ImageField(upload_to="photos", verbose_name='Фото2', blank=True)
    photo2 = models.ImageField(upload_to="photos", verbose_name='Фото3', blank=True)
    photo3 = models.ImageField(upload_to="photos", verbose_name='Фото4', blank=True)
    photo4 = models.ImageField(upload_to="photos", verbose_name='Фото5', blank=True)
    center = models.CharField(max_length=255, verbose_name='Координата', blank=True, null=True)
    scale = models.CharField(max_length=255, verbose_name='Маштаб', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title


class CommentNew(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.PROTECT, blank=True, null=True)
    username = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_name', blank=True, null=True)
    body = models.TextField(verbose_name='Комментарий')
    photo = models.ImageField(upload_to="photos", verbose_name='Фото', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.username, self.post)

