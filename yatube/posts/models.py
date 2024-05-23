from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    """Класс для описания сообществ"""
    title = models.CharField('Имя', max_length=200)
    slug = models.SlugField('Адрес', unique=True)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Сообщества'


class Post(models.Model):
    """Класс для описания записей/постов"""
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Сообщество'
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


