# Generated by Django 4.1 on 2022-12-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0019_remove_courses_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='photo',
            field=models.FileField(default='', upload_to='media/media/static'),
        ),
    ]
