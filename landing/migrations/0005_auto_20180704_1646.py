# Generated by Django 2.0.6 on 2018-07-04 13:46

from django.db import migrations, models
import helpers


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20180704_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authormodel',
            name='landscapeImg',
            field=models.ImageField(upload_to='author/landscape', validators=[helpers.isLandscape], verbose_name='Изображение для больших экранов'),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='portraitImg',
            field=models.ImageField(upload_to='author/portrait', validators=[helpers.isPortrait], verbose_name='Изображение для смартфонов и телефонов'),
        ),
        migrations.DeleteModel(
            name='authorLandscapeImages',
        ),
        migrations.DeleteModel(
            name='authorPortraitImages',
        ),
    ]
