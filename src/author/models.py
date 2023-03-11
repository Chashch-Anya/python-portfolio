from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения информации об авторе
    """

    resume = models.URLField(verbose_name="Ссылки на резюме")
    github = models.URLField(verbose_name="GitHub")
    email = models.EmailField(verbose_name="Электронная почта")

    class Meta:
        verbose_name = "Информация об авторе"
        verbose_name_plural = "Информация об авторе"

    def __str__(self) -> str:
        return f'Объект "Инофрмация об авторе" (id={self.pk})'
    