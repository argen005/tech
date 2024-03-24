from django.db import models

class Enterprise(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    location =models.CharField(verbose_name="Адрес", max_length=100)
    opening_hours = models.TimeField(verbose_name="Время открытия", null=True, blank=True)
    closing_hours = models.TimeField(verbose_name="Время закрытия", null=True, blank=True)
    is_24_7 = models.BooleanField(verbose_name="Круглосуточно", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    expiration_date = models.DateField(verbose_name="Срок годности", null=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


