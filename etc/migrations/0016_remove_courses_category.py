# Generated by Django 4.1 on 2022-12-08 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0015_category_courses_photo_courses_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='category',
        ),
    ]
