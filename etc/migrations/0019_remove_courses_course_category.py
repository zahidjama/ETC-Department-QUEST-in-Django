# Generated by Django 4.1 on 2022-12-08 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0018_courses_category_courses_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='course_category',
        ),
    ]
