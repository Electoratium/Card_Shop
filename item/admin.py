from django.contrib import admin
from .models import *
from .forms import *

class ItemImagesInline(admin.TabularInline):
    model = ItemImages
    min_num = 2
    max_num = 5
    extra = 0



class ItemAdmin(admin.ModelAdmin):
    form = ItemForm

    list_display = ['name', 'price', 'created', 'isActive']

    inlines = [ItemImagesInline]

    class Meta:
        model = ItemModel


admin.site.register(ItemModel, ItemAdmin)

class ItemImagesAdmin(admin.ModelAdmin):
    list_display = ['item', 'created', 'updated']

    class Meta:
        model = ItemImages

admin.site.register(ItemImages, ItemImagesAdmin)

class GeneralSettingsAdmin(admin.ModelAdmin):
    form = GeneralDetailsForm

    list_display = [field.name for field in GeneralDetails._meta.fields]

    class Meta:
        model = GeneralDetails


    def has_add_permission(self, request):
        if GeneralDetails.objects.count() + 1 > 1:
            return False
        return True


admin.site.register(GeneralDetails, GeneralSettingsAdmin)


class OrdersAdmin(admin.ModelAdmin):
    form = OrderForm

    list_display = [field.name for field in Orders._meta.fields]

    class Meta:
        model = Orders


admin.site.register(Orders, OrdersAdmin)
