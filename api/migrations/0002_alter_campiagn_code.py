# Generated by Django 4.1.3 on 2022-12-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campiagn',
            name='code',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]