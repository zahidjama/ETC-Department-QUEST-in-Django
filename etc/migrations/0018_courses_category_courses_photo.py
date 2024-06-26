# Generated by Django 4.1 on 2022-12-08 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0017_remove_courses_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='etc.category'),
        ),
        migrations.AddField(
            model_name='courses',
            name='photo',
            field=models.FileField(default='', upload_to='../media/media/static'),
        ),
    ]
