# Generated by Django 4.2.4 on 2023-08-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
