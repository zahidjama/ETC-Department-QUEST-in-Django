# Generated by Django 2.2.12 on 2022-07-30 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='img',
            field=models.ImageField(default='', upload_to='../media/media/static/'),
        ),
    ]