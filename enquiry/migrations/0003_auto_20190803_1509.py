# Generated by Django 2.2.4 on 2019-08-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0002_auto_20190803_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='shift',
            field=models.ManyToManyField(to='enquiry.Shift'),
        ),
    ]
