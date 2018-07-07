from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def isLandscape(imageObj):
    width, height = get_image_dimensions(imageObj)

    if (width < height):
        raise ValidationError('Неправильная ориентация изображения, необходима не портретная ориентация')

def isPortrait(imageObj):
    width, height = get_image_dimensions(imageObj)

    if( width > height ):
        raise ValidationError('Неправильная ориентация изображения, необходима портретная ориентация')