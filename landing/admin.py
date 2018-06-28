from django.contrib import admin
from .models import *

class SliderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'description', 'created', 'isActive']
    fields = ('landscapeImage', 'portraitImage', 'title', 'description', 'isActive')


    class Meta:
        model = Slides


admin.site.register(Slides, SliderAdmin)