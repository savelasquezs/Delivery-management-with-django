# Generated by Django 4.1 on 2022-08-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_producto_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
