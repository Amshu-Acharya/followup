# Generated by Django 2.2.4 on 2019-08-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0006_course_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='php', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
