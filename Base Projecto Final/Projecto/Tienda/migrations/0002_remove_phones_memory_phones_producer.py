# Generated by Django 4.0.6 on 2022-08-15 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phones',
            name='memory',
        ),
        migrations.AddField(
            model_name='phones',
            name='producer',
            field=models.CharField(default='Motorola', max_length=100),
            preserve_default=False,
        ),
    ]
