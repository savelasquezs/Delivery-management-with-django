# Generated by Django 4.0.4 on 2022-08-17 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='pet_particulares',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
