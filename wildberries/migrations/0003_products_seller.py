# Generated by Django 4.0.4 on 2022-07-17 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildberries', '0002_products_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='seller',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='wildberries.sellers', verbose_name='Продавец'),
            preserve_default=False,
        ),
    ]