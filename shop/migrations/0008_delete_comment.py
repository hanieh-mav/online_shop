# Generated by Django 3.1.4 on 2021-02-17 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]