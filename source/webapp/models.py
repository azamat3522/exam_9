from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos', null=False, blank=False, verbose_name='Фотография')
    signature = models.CharField(max_length=100, null=False, blank=False, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата-время создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos', verbose_name='Автор')
    count_likes = models.IntegerField(default=0, verbose_name='Количество лайков')

    def __str__(self):
        return self.signature

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Comment(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments', verbose_name='Фотография')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата-время создания')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'





