# Generated by Django 3.0.2 on 2020-04-20 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ContactManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='occupation',
        ),
        migrations.AlterField(
            model_name='contact',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
