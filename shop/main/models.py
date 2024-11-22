from django.db import models
from django.contrib.auth.models import AbstractUser

class categories(models.Model):
    name = models.CharField('Категория', max_length=100, unique=True)
    slug = models.SlugField('URL', max_length=100, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class products(models.Model):
    product_name = models.CharField('Название', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True, null=True)
    img = models.ImageField('Изображение', upload_to='images', blank=True, null=True)
    img2 = models.ImageField('Изображение2', upload_to='images', blank=True, null=True)
    img3 = models.ImageField('Изображение3', upload_to='images', blank=True, null=True)
    img4 = models.ImageField('Изображение4', upload_to='images', blank=True, null=True)
    img5 = models.ImageField('Изображение5', upload_to='images', blank=True, null=True)
    product_price = models.DecimalField('Цена', max_digits=7, decimal_places=2, default=0.00)
    discount = models.DecimalField('Скидка', max_digits=7, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField('Количество', default=0)
    slug = models.SlugField('URL', max_length=100, unique=True, blank=True, null=True)
    category = models.ForeignKey(to=categories, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.product_name
    
    def display_id(self):
        return f"{self.id:03}"
    
    def sell_price(self):
        if self.discount:
            return round(self.product_price - self.product_price*self.discount/100)

        return self.product_price
    
    def usd_price(self):
        if self.discount:
            return round(float(self.product_price) * 0.01 - float(self.product_price) * 0.01 * float(self.discount)/100, 2)
        
        return round(float(self.product_price) * 0.01, 2)

       
    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class User(AbstractUser):
    image = models.ImageField('Аватар', upload_to='images', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=100, null=True, blank=True, verbose_name="Область/край/регион")
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Город")
    street = models.CharField(max_length=100, null=True, blank=True, verbose_name="Улица/дом/квартира")
    postcode = models.CharField(max_length=100, null=True, blank=True, verbose_name="Почтовый индекс")

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
