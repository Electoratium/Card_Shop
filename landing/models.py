from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.core.exceptions import ValidationError, PermissionDenied
from django.core.files.images import get_image_dimensions

from os import path
from uuid import uuid4
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

from django.dispatch import receiver
from django.db.models.signals import post_init






def convertImagesType(CollectionImages, filetype):


    for imageObj in CollectionImages:
        newImgName = 'img-%s.%s' % (uuid4(), filetype)

        oldFileName = path.basename(imageObj.name)

        filename, curFileType = oldFileName.split('.')

        if curFileType != filetype:

            newImage = Image.open(imageObj)
            newImageIo = BytesIO()
            newImage.save(newImageIo, format = filetype)


            imageObj.delete(save=False)

            imageObj.save (
                newImgName,
                content = ContentFile(newImageIo.getvalue()),
                save = False
            )

        else:
            imageObj.save (
                newImgName,
                imageObj,
                save = False
            )



def isLandscape(imageObj):
    width, height = get_image_dimensions(imageObj)

    if (width < height):
        raise ValidationError('Неправильная ориентация изображения, необходима портретная ориентация')

def isPortrait(imageObj):
    width, height = get_image_dimensions(imageObj)

    if( width > height ):
        raise ValidationError('Неправильная ориентация изображения, необходима не портретная ориентация')



class SlidesModel(models.Model):

    landscapeImage = models.ImageField("Изображение для больших экранов", validators = [isLandscape], upload_to = 'slider-content/large', blank = False)
    portraitImage = models.ImageField("Изображение для смартфонов и телефонов", validators = [isPortrait], upload_to = 'slider-content/small', blank = False)
    title = models.CharField("Заголовок", max_length = 24, blank=True)
    description = models.CharField("Описание", max_length = 128, blank=True, default = None)
    created = models.DateTimeField("Дата создания", auto_now_add = True, auto_now = False)
    isActive = models.BooleanField("Показывать слайд", default = True)


    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return "Слайд %s" % self.id


    def save(self, *args, **kwargs):
        convertImagesType([self.landscapeImage, self.portraitImage], 'jpeg')

        super(SlidesModel, self).save(*args, **kwargs)



class AuthorModel(models.Model):
    landscapeImage = models.ImageField("Изображение для больших экранов", validators = [isLandscape],
                                       upload_to = 'author/large')
    portraitImage = models.ImageField("Изображение для смартфонов и телефонов", validators = [isPortrait],
                                      upload_to = 'author/small')
    authorName = models.CharField("Имя",  default = 'Виктория Ратеева', max_length = 24)
    authorJob = models.CharField("Ученая степень, место работы и т.д.", max_length = 64)
    authorDescription = models.CharField("Описание", max_length = 256)
    authorPhone = PhoneNumberField("Телефон рабочий")
    authorPhoneAdd = PhoneNumberField("Доп. телефон", blank = True)
    authorEmail = models.EmailField("Email", default = "ratviktoriya@gmail.com", max_length = 24)



    class Meta:
        verbose_name = "Информация об авторе"
        verbose_name_plural = "Информация об авторе"

    def __str__(self):
        return "Автор: %s" % self.authorName

    def save(self, *args, **kwargs):
        convertImagesType([self.landscapeImage, self.portraitImage], 'png')

        super(AuthorModel, self).save(*args, **kwargs)