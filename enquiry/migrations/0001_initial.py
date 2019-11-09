# Generated by Django 2.2.7 on 2019-11-07 15:51

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('cost', models.PositiveIntegerField()),
                ('duration', models.DurationField()),
                ('extra_information', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='course')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('excerpt', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('latest_eduation', models.CharField(max_length=200)),
                ('preferred_eduation', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry_date', models.DateTimeField(auto_now_add=True)),
                ('courses', models.ManyToManyField(related_name='enquires', to='enquiry.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_shifts', to='enquiry.Course')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_shifts', to='enquiry.Shift')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='shifts',
            field=models.ManyToManyField(through='enquiry.CourseShift', to='enquiry.Shift'),
        ),
    ]
