# Generated by Django 4.2.1 on 2023-05-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_alter_post_photo_alter_post_photo1_alter_post_photo2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='center_x',
            field=models.FloatField(null=True, verbose_name='Координата 1'),
        ),
        migrations.AddField(
            model_name='post',
            name='center_y',
            field=models.FloatField(null=True, verbose_name='Координата 2'),
        ),
    ]
