from django.db import models

from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

from os import path
from re import sub
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile




def convertTypeFile(imageObj, filetype):
    oldFileName = path.basename(imageObj.name)

    filename, format = oldFileName.split('.')

    if format != filetype:


        print('gg')

        newImage = Image.open(imageObj)

        newImageIo = BytesIO()
        newImage.save(newImageIo, format = filetype)

        newFileName = sub('\.(.*)$', '.%s' % (filetype), oldFileName)

        imageObj.delete(save=False)

        imageObj.save(
        newFileName,
        content=ContentFile(newImageIo.getvalue()),
        save=False
        )

        return imageObj

    return imageObj








    # imagePath = imageFile
    # filename, prefix = path.splitext(str(imageFile))
    #
    # if prefix != filetype:
    #     newImageFile = Image.open(imagePath)
    #     imagePath = newImageFile.save("%s%s" % (filename, filetype))
    #



def validateOrientationImage(imageFile, orientation):
    width, height = get_image_dimensions(imageFile)
    if width < height and orientation == 'landscape':
        raise ValidationError('Неправильная ориентация изображения, необходима непортретная ориентация')
    elif width > height and orientation == 'portrait':
        raise ValidationError('Неправильная ориентация изображения, необходима портретная ориентация')



class Slides(models.Model):
    landscapeImage = models.ImageField("Изображение для больших экранов", validators=[lambda value: validateOrientationImage(value, 'landscape')], upload_to = 'slider-content/large', blank = False)
    portraitImage = models.ImageField("Изображение для смартфонов и телефонов", validators=[lambda value: validateOrientationImage(value, 'portrait')], upload_to = 'slider-content/small', blank = False)
    title = models.CharField("Заголовок", max_length = 24, blank=True)
    description = models.CharField("Описание", max_length = 128, blank=True, default = None)
    created = models.DateTimeField("Дата создания", auto_now_add = True, auto_now = False)
    isActive = models.BooleanField("Показывать слайд", default = True)


    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return "Слайд %s" % (self.id)


    def save(self, *args, **kwargs):
        convertTypeFile(self.landscapeImage, 'png')


        super(Slides, self).save(*args, **kwargs)