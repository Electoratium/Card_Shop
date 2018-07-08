from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe


from helpers import *


class LandscapeImageSlider(models.Model):
    image = models.ImageField("Изображение для больших экранов", validators = [isLandscape], upload_to = 'slider-content/landscape', blank = False)
    created = models.DateTimeField("Дата создания", auto_now_add = True, auto_now = False)

    def image_tag(self):
        return mark_safe('<img src="%s" width="250" height="150" />' % self.image.url)

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Не портретное изображение слайдера'
        verbose_name_plural = 'Не портретные изображения слайдера'

    def __str__(self):
        return "Изображение %s" % self.pk


class PortraitImageSlider(models.Model):
    image = models.ImageField("Изображение для смартфонов и телефонов", validators = [isPortrait], upload_to = 'slider-content/portrait', blank = False)
    created = models.DateTimeField("Дата создания", auto_now_add = True, auto_now = False)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="250" />' % (self.image.url))

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Портретное изображение слайдера'
        verbose_name_plural = 'Портретные изображения слайдера'

    def __str__(self):
        return "Изображение %s" % self.pk


class SlidesModel(models.Model):
    landscapeImg = models.ForeignKey(LandscapeImageSlider, verbose_name='Не портретное изображение', null = True, on_delete = models.SET_NULL)
    portraitImg = models.ForeignKey(PortraitImageSlider, verbose_name = 'Портретное изображение', null = True, on_delete = models.SET_NULL)
    title = models.CharField("Заголовок", max_length = 24, blank=True)
    description = models.CharField("Основной текст", max_length = 128, blank=True, default = None)
    created = models.DateTimeField("Дата создания", auto_now_add = True, auto_now = False)
    isActive = models.BooleanField("Показывать слайд", default = True)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return "Слайд %s" % self.pk


class authorLandscapeImages(models.Model):
    image = models.ImageField("Не портретное изображение", validators = [isLandscape],
                                       upload_to = 'author/landscape')
    created = models.DateTimeField("Дата создания", auto_now_add = True, auto_now = False)

    def image_tag(self):
        return mark_safe('<img src="%s" width="250" height="250" />' % (self.image.url))

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Не портретное изображение автора'
        verbose_name_plural = 'Не портретные изображения автора'

    def __str__(self):
        return "Изображение %s" % self.pk


class authorPortraitImages(models.Model):
    image = models.ImageField("Портретное изображение", validators = [isPortrait],
                                      upload_to = 'author/portrait')
    created = models.DateTimeField("Дата создания", auto_now_add = True, auto_now = False)

    def image_tag(self):
        return mark_safe('<img src="%s" width="200" height="250" />' % (self.image.url))

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Портретное изображение автора'
        verbose_name_plural = 'Портретные изображения автора'

    def __str__(self):
        return "Изображение %s" % self.pk



class AuthorModel(models.Model):
    landscapeImg = models.ForeignKey('authorLandscapeImages', verbose_name='Не портретное изображение', null=True,
                                     on_delete=models.SET_NULL)
    portraitImg = models.ForeignKey('authorPortraitImages', verbose_name='Портретное изображение', null=True,
                                    on_delete=models.SET_NULL)
    authorName = models.CharField("Имя",  default = 'Виктория Ратеева', max_length = 24)
    authorJob = models.CharField("Место работы, ученая степень и т.д.", max_length = 64)
    authorDescription = models.CharField("Описание", max_length = 256, default = None)

    authorPhone = PhoneNumberField("Телефон рабочий")
    authorPhoneAdd = PhoneNumberField("Доп. телефон", blank = True)
    authorEmail = models.EmailField("Email", default = "ratviktoriya@gmail.com", max_length = 24)

    class Meta:
        verbose_name = "Информация об авторе"
        verbose_name_plural = "Информация об авторе"

    def __str__(self):
        return "Автор: %s" % self.authorName
