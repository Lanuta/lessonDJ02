from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст новости")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")  # связь с пользователем



    def __str__(self):
        return self.title
        return self.content
        return self.created_at
        return self.updated_at
        return self.author
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
