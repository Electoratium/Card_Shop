from django.shortcuts import render
from .models import *


def landing(request):
    slides = SlidesModel.objects.filter(isActive=True).order_by('created')
    aboutAuthor = AuthorModel.objects.all().first()

    return render(request, 'landing.html', {'slides': slides, 'aboutAuthor': aboutAuthor})


def item(request):
    return render(request, 'item.html')