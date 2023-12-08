from django.db import models


class Offer(models.Model):
    model = models.CharField("Модель устройства", max_length=5)
    price = models.FloatField("Цена")
    description = models.TextField("Описание")
    condition = models.BooleanField("Б/У", default=False)
    photo = models.ImageField(
        "Фотография устройства",
        help_text="Желательно несколько фотографий с разных ракурсов",
        upload_to='images/', default=None)
