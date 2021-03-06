# Generated by Django 2.0.6 on 2018-07-04 11:06

from django.db import migrations, models
import django.db.models.deletion
import helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='itemImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landscapeImage', models.ImageField(upload_to='items/landscape', validators=[helpers.isLandscape], verbose_name='Не Портретное изображение')),
                ('portraitImage', models.ImageField(upload_to='items/portrait', validators=[helpers.isPortrait], verbose_name='Портретное изображение')),
                ('smallImage', models.ImageField(upload_to='items/itemsSlider', validators=[helpers.isPortrait], verbose_name='Маленькое портретное изображение для слайдера товаров')),
                ('isActive', models.BooleanField(default=True, verbose_name='Показывать изображения')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='itemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название товара')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('description', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('isActive', models.BooleanField(default=True, verbose_name='Отображать товар')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='itemimages',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='item.itemModel'),
        ),
    ]
