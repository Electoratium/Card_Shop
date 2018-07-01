from django.contrib import admin
from .models import *










class SliderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'description', 'created', 'isActive']
    fields = ('landscapeImage', 'portraitImage', 'title', 'description', 'isActive')
    list_filter = ['isActive']
    ordering = ['isActive']


    class Meta:
        model = SlidesModel


    def has_add_permission(self, request):
        maxSlides = 5
        if not SlidesModel.objects.filter(isActive=True).count() < maxSlides:
            return False
        return True






admin.site.register(SlidesModel, SliderAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['authorName', 'authorJob', 'authorDescription', 'authorPhone']
    fieldsets = (
        (None, {
            'fields': ('landscapeImage', 'portraitImage')
        }),
        ('Основные данные', {
            'fields': ('authorName', 'authorJob', 'authorDescription')
        }),
        ('Контактные данные', {
            'fields': ('authorPhone', 'authorPhoneAdd', 'authorEmail')
        }),
    )



    class Meta:
        model = AuthorModel

    def has_add_permission(self, request):
        if AuthorModel.objects.count() + 1 > 1:
            return False
        return True

admin.site.register(AuthorModel, AuthorAdmin)