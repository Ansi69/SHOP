from django.db import models

class products(models.Model):
    product_name = models.CharField('Название', max_length=100)
    product_price = models.IntegerField('Цена', max_length=100)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'