# Generated by Django 3.2.4 on 2021-06-29 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]