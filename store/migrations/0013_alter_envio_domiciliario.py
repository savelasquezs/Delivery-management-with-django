# Generated by Django 4.1 on 2022-08-30 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_envio_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='domiciliario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.usuario'),
        ),
    ]
