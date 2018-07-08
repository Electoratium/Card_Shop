from django import forms
from .models import Orders, ItemModel, GeneralDetails, Orders



class ItemForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs = {'rows': 5, 'maxlength': 400}), label = 'Описание')
    class Meta:
        model = ItemModel
        exclude = ['created', 'updated']


class GeneralDetailsForm(forms.ModelForm):
    sendingDetails = forms.CharField(widget=forms.Textarea(attrs = {'rows': 5, 'maxlength': 320}), label = 'Детали отправки', help_text = 'Будет отображаться на всех товарах')
    class Meta:
        model = GeneralDetails
        fields = [field.name for field in GeneralDetails._meta.fields]




class OrderForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs = {'rows': 5, 'maxlength': 64}), label = '"Текст заказа"')
    class Meta:
        model = Orders
        exclude = ['created']


class OrderFormTemplate(forms.ModelForm):
    class Meta:
        model = Orders
        exclude = ['item', 'created', 'IsProcessed']

    def __init__(self, *args, **kwargs):
        super(OrderFormTemplate, self).__init__(*args, **kwargs)

        for fieldName, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'