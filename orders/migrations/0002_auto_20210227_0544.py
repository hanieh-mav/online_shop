# Generated by Django 3.1.6 on 2021-02-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['is_paid', 'is_send', '-created']},
        ),
        migrations.AddField(
            model_name='order',
            name='is_send',
            field=models.BooleanField(default=False),
        ),
    ]
