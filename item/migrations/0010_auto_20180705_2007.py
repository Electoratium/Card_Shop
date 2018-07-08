# Generated by Django 2.0.6 on 2018-07-05 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_auto_20180705_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimages',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='item.ItemModel'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Товар', to='item.ItemModel'),
        ),
    ]
