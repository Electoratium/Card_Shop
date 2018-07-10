from django.db import models
from helpers import *

class ItemModel(models.Model):
    name = models.CharField('Название товара', max_length = 64)
    price = models.IntegerField('Цена', default= 0)
    description = models.CharField("Описание товара", max_length = 400)
    created = models.DateTimeField("Дата создания", auto_now_add = True, auto_now = False)
    updated = models.DateTimeField("Дата изменения", auto_now_add = False, auto_now = True)

    isActive = models.BooleanField("Отображать товар", default = True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return '%s: %s грн.' % (self.name, self.price)



class ItemImages(models.Model):
    item = models.ForeignKey(ItemModel, on_delete = models.SET_NULL, null=True)
    landscapeImage = models.ImageField("Не Портретное изображение", validators = [isLandscape], upload_to = 'items/landscape')
    portraitImage = models.ImageField("Портретное изображение", validators = [isPortrait], upload_to = 'items/portrait')
    smallImage = models.ImageField("Маленькое портретное изображение для слайдера товаров", validators = [isPortrait], upload_to = 'items/itemsSlider')
    isActive = models.BooleanField("Показывать изображения", default = True)

    created = models.DateTimeField("Дата создания", auto_now_add = True, auto_now = False)
    updated = models.DateTimeField("Дата изменения", auto_now_add = False, auto_now = True)


    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return 'Изображение %s' % self.pk



class GeneralDetails(models.Model):
    sendingDetails = models.CharField('Детали отправки', max_length = 320)
    workEmail = models.EmailField('Еmail на который будут приходить оповещения о покупателях', default = 'ratviktoriya@gmail.com', max_length = 24)


    class Meta:
        verbose_name = 'Детали по товару'
        verbose_name_plural = 'Общие детали по товару'

    def __str__(self):
        return 'Настройка по товару'



class Orders(models.Model):
    text = models.CharField(max_length = 64, blank = True)
    name = models.CharField("Имя", max_length = 24)
    email = models.EmailField("Email", max_length = 32)
    phone = models.CharField("Номер телефона", blank = True, max_length = 10)
    item = models.ForeignKey(ItemModel, related_name = "Товар", on_delete = models.SET_NULL, null = True)
    created = models.DateTimeField("Дата создания", auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return "Заказ № %s от %s" % (self.pk, self.created.strftime("%d %b %H:%M"))





