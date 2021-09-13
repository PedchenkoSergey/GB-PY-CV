from django.db import models

# Create your models here.


class GoodModel(models.Model):
    MEASURE_CHOICES = [
        ('ШТ', 'Шт.'),
        ('УПАК', 'Упак.'),
        ('КОР', 'Кор.'),
    ]

    title = models.CharField(
        verbose_name="Название",
        max_length=255
    )
    created_date = models.DateTimeField(
        verbose_name="Дата Поступления",
        auto_created=True,
        auto_now_add=True
    )

    price = models.PositiveIntegerField(
        verbose_name="Цена",
        default=0
    )

    measure = models.CharField(
        max_length=4,
        choices=MEASURE_CHOICES
    )

    vendor = models.CharField(
        verbose_name="Поставщик",
        max_length=255
    )

    def __str__(self):
        return f"{self.title} | {self.vendor}"

    class Meta:
        verbose_name = "Карточка товара"
        verbose_name_plural = "Карточки товаров"
