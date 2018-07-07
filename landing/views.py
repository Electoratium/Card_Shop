from django.shortcuts import render
from .models import *

from item.models import *


def landing(request):
    slides = SlidesModel.objects.filter(isActive=True).order_by('created')
    aboutAuthor = AuthorModel.objects.first()


    items = ItemImages.objects.filter(isActive = True).filter(item__isActive = True).distinct('item__name')

    newArrivals = items[:3]

    return render(request, 'landing.html', {'slides': slides, 'aboutAuthor': aboutAuthor, 'newArrivals': newArrivals, 'items': items})