# Generated by Django 2.2.4 on 2019-08-21 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20190821_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
