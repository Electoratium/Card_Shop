# Generated by Django 2.0.4 on 2018-06-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landscapeImage', models.ImageField(upload_to='slider-content/large', verbose_name='Изображение для больших экранов')),
                ('portraitImage', models.ImageField(upload_to='slider-content/small', verbose_name='Изображение для смартфонов и телефонов')),
                ('title', models.CharField(blank=True, max_length=24, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, default=None, max_length=128, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('isActive', models.BooleanField(default=True, verbose_name='Показывать слайд')),
            ],
            options={
                'verbose_name_plural': 'Слайды',
                'verbose_name': 'Слайд',
            },
        ),
        migrations.DeleteModel(
            name='Sliders',
        ),
    ]
