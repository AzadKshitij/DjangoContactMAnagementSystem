# Generated by Django 3.0.2 on 2020-04-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='info',
            field=models.CharField(default='Author', max_length=200),
        ),
    ]
