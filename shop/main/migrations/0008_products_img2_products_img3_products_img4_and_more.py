# Generated by Django 5.1.1 on 2024-11-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение2'),
        ),
        migrations.AddField(
            model_name='products',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение3'),
        ),
        migrations.AddField(
            model_name='products',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение4'),
        ),
        migrations.AddField(
            model_name='products',
            name='img5',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение5'),
        ),
    ]