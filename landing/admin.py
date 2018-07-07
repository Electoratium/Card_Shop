from django.contrib import admin
from .models import *
from .forms import *


class SliderAdmin(admin.ModelAdmin):
    form = SlidesForm

    list_display = ['pk', 'title', 'description', 'created', 'isActive']
    exclude = ['created']
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


class LandscapeSliderImgAdmin(admin.ModelAdmin):
    list_display = ['pk', 'image', 'created']

    fields = ['image', 'image_tag']
    readonly_fields = ['image_tag']

    class Meta:
        model = LandscapeImageSlider


admin.site.register(LandscapeImageSlider, LandscapeSliderImgAdmin)


class PortraitSliderImgAdmin(admin.ModelAdmin):
    list_display = ['pk', 'image', 'created']

    fields = ['image', 'image_tag']
    readonly_fields = ['image_tag']

    class Meta:
        model = PortraitImageSlider


admin.site.register(PortraitImageSlider, PortraitSliderImgAdmin)


class LandscapeAuthorImgAdmin(admin.ModelAdmin):
    list_display = ['pk', 'image', 'created']

    fields = ['image', 'image_tag']
    readonly_fields = ['image_tag']

    class Meta:
        model = authorLandscapeImages


admin.site.register(authorLandscapeImages, LandscapeAuthorImgAdmin)


class PortraitAuthorImgAdmin(admin.ModelAdmin):
    list_display = ['pk', 'image', 'created']

    fields = ['image', 'image_tag']
    readonly_fields = ['image_tag']

    class Meta:
        model = authorPortraitImages


admin.site.register(authorPortraitImages, PortraitAuthorImgAdmin)


class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm

    list_display = ['authorName', 'authorJob', 'authorDescription', 'authorPhone']
    fieldsets = (
        (None, {
            'fields': ('landscapeImg', 'portraitImg')
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
