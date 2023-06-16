# Generated by Django 4.2.1 on 2023-05-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_alter_post_photo_alter_post_photo1_alter_post_photo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото1'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото2'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото3'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото4'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото5'),
        ),
    ]
