# Generated by Django 3.0.8 on 2020-08-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myawsmCart', '0002_auto_20200802_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='', upload_to='foodsite/images'),
        ),
    ]
