# Generated by Django 3.1.6 on 2021-02-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210215_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_subcat',
            field=models.BooleanField(default=False),
        ),
    ]
