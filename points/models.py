import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def generate_share_slug() -> str:
    """
    Метод, который генерирует случайный уникальный slug-идентификатор
    :return: строка из 32 символов в формате hex, например:
             '9f3c1a2b7e124cf5a29c8c9a0f50e27d'
    """
    return uuid.uuid4().hex


class Point(models.Model):
    """
    Модель для точек
    """
    title = models.CharField("Название", max_length=255, blank=True, default="")
    latitude = models.DecimalField(
        "Широта", max_digits=20, decimal_places=17,
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )
    longitude = models.DecimalField(
        "Долгота", max_digits=20, decimal_places=17,
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )

    class Meta:
        verbose_name = "Точка"
        verbose_name_plural = "Точки"
        indexes = [models.Index(fields=["latitude", "longitude"])]

    def __str__(self):
        return f"{self.title} {self.latitude}:{self.longitude}"


class Share(models.Model):
    """
    Подборка точек, доступная по ссылке /map/<slug>/
    """
    slug = models.SlugField(
        "Слаг", max_length=36, unique=True, default=generate_share_slug
    )
    title = models.CharField("Название", max_length=255, blank=True, default="")
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    points = models.ManyToManyField(Point, related_name="shares")

    class Meta:
        verbose_name = "Подборка (Share)"
        verbose_name_plural = "Подборки (Shares)"

    def __str__(self):
        return f"Share {self.slug} ({self.title or 'без названия'})"
