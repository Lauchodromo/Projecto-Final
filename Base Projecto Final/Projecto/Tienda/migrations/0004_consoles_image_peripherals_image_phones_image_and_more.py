# Generated by Django 4.0.6 on 2022-08-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0003_peripherals_alter_consoles_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consoles',
            name='image',
            field=models.ImageField(blank=True, upload_to='console_images/'),
        ),
        migrations.AddField(
            model_name='peripherals',
            name='image',
            field=models.ImageField(blank=True, upload_to='peripheral_images/'),
        ),
        migrations.AddField(
            model_name='phones',
            name='image',
            field=models.ImageField(blank=True, upload_to='phone_images/'),
        ),
        migrations.AlterField(
            model_name='games',
            name='image',
            field=models.ImageField(blank=True, upload_to='game_images/'),
        ),
    ]