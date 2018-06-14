from django.shortcuts import render


def landing(request):
    return render(request, 'new_html/landing.html')


def item(request):
    return render(request, 'item.html')