# Generated by Django 4.0.4 on 2022-05-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
    ]