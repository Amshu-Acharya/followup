# Generated by Django 2.2.7 on 2019-11-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0002_auto_20191107_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
